import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from solve_with_ai import AISolutionGenerator

class TestAISolutionGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AISolutionGenerator()
        self.sample_problem = {
            "title": "Two Sum",
            "content": "Find two numbers that add up to target.",
            "difficulty": "Easy",
            "hints": ["Use a hash map"],
            "code_template": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass"
        }

    def test_create_prompt(self):
        prompt = self.generator.create_prompt(self.sample_problem, ["Python"])
        self.assertIn("Two Sum", prompt)
        self.assertIn("Easy", prompt)
        self.assertIn("Use a hash map", prompt)
        self.assertIn("class Solution", prompt)
        self.assertIn("Format as JSON", prompt)

    def test_detect_indent_unit(self):
        code_4_spaces = "def foo():\n    print('bar')"
        self.assertEqual(self.generator._detect_indent_unit(code_4_spaces), 4)
        
        code_2_spaces = "function foo() {\n  console.log('bar');\n}"
        self.assertEqual(self.generator._detect_indent_unit(code_2_spaces), 2)
        
        code_mixed = "def foo():\n  print('bar')" # 2 spaces
        self.assertEqual(self.generator._detect_indent_unit(code_mixed), 2)

    @patch.object(AISolutionGenerator, '_load_snippet')
    def test_clean_code_with_snippet_match(self, mock_load_snippet):
        # Case: Java with 9 spaces excess (Groq bug), Template has 4 spaces
        template = "class Solution {\n    public int countUnguarded(int m, int n) {\n        \n    }\n}"
        mock_load_snippet.return_value = template
        
        # AI output has 9 spaces indent for method body (4 original + 5 extra? No, usually 4 + 7 = 11 or 0 + 9 = 9)
        # Let's simulate the Java case: 
        # Template: 4 spaces
        # AI: 13 spaces (4 + 9)
        ai_code = "class Solution {\n             public int countUnguarded(int m, int n) {\n                 int count = 0;\n             }\n}"
        
        cleaned = self.generator._clean_code(ai_code, "problem-slug", "java")
        
        # Expectation: Excess 9 removed. 13 - 9 = 4 spaces.
        expected = "class Solution {\n    public int countUnguarded(int m, int n) {\n        int count = 0;\n    }\n}"
        self.assertEqual(cleaned.strip(), expected.strip())

    @patch.object(AISolutionGenerator, '_load_snippet')
    def test_clean_code_fallback_indent_unit(self, mock_load_snippet):
        # Case: JS with 11 spaces excess (Groq bug), Template has 0 spaces for function line
        # Template
        template = "var countUnguarded = function(m, n, guards, walls) {\n    \n};"
        mock_load_snippet.return_value = template
        
        # AI output: First line 0 indent, second line 11 indent (4 original + 7 bug)
        ai_code = "var countUnguarded = function(m, n, guards, walls) {\n           let grid = [];\n           return 0;\n       };"
        
        cleaned = self.generator._clean_code(ai_code, "problem-slug", "javascript")
        
        # Expectation: 
        # Snippet match fails for 2nd line (not in template).
        # Fallback logic sees 11 spaces excess.
        # Indent unit detected as 4 (from template).
        # 11 - 4 = 7 (valid bug range).
        # Removes 7 spaces. Result: 4 spaces.
        expected = "var countUnguarded = function(m, n, guards, walls) {\n    let grid = [];\n    return 0;\n};"
        self.assertEqual(cleaned.strip(), expected.strip())

    def test_clean_code_basic(self):
        raw_code = "```python\nprint('hello')\n```"
        cleaned = self.generator._clean_code(raw_code)
        self.assertEqual(cleaned, "print('hello')")

        raw_code_indented = "    print('hello')"
        cleaned = self.generator._clean_code(raw_code_indented)
        self.assertEqual(cleaned, "print('hello')")

    def test_parse_json_response_valid(self):
        json_response = """
        Here is the solution:
        ```json
        {
            "approach": "Hash Map",
            "time_complexity": "O(n)",
            "space_complexity": "O(n)",
            "solutions": {
                "python": "print('hello')"
            }
        }
        ```
        """
        parsed = self.generator.parse_json_response(json_response)
        self.assertEqual(parsed["approach"], "Hash Map")
        self.assertEqual(parsed["solutions"]["python"], "print('hello')")

    def test_parse_json_response_fallback(self):
        # Missing code blocks but valid JSON
        json_response = """
        {
            "approach": "Hash Map",
            "solutions": {
                "python": "print('hello')"
            }
        }
        """
        parsed = self.generator.parse_json_response(json_response)
        self.assertEqual(parsed["approach"], "Hash Map")

    def test_merge_solutions(self):
        base = {"solutions": {"python": "old"}}
        new = {
            "approach": "Better Approach",
            "solutions": {"cpp": "new cpp"}
        }
        self.generator._merge_solutions(base, new)
        self.assertEqual(base["approach"], "Better Approach")
        self.assertEqual(base["solutions"]["python"], "old")
        self.assertEqual(base["solutions"]["cpp"], "new cpp")

    @patch.object(AISolutionGenerator, "_generate_content")
    def test_solve_with_gemini_mock(self, mock_generate):
        # Setup Mock
        mock_response = MagicMock()
        mock_response.candidates = [MagicMock()]
        mock_response.candidates[0].finish_reason = 1
        mock_response.text = json.dumps({
            "approach": "Mock Approach",
            "solutions": {"python": "print('mock')"}
        })
        # Mock usage metadata
        mock_usage = MagicMock()
        mock_usage.prompt_token_count = 10
        mock_usage.candidates_token_count = 20
        mock_usage.total_token_count = 30
        mock_response.usage_metadata = mock_usage

        mock_generate.return_value = mock_response

        self.generator.client = MagicMock()

        result = self.generator.solve_with_gemini(self.sample_problem)

        self.assertIsNotNone(result)
        self.assertIn("solutions", result)
        self.assertIn("python", result["solutions"])
        self.assertIn("elapsed_time", result)
        self.assertGreaterEqual(result["elapsed_time"], 0.0)

if __name__ == '__main__':
    unittest.main()
