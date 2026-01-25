
import unittest
import os
import shutil
import json
from scripts.generate_post import PostGenerator

class TestPostGenerator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "_posts/_test_gen"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        self.generator = PostGenerator(posts_dir=self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_liquid_syntax_escaping(self):
        """Test Case 1: Verify that code containing {{ and }} is wrapped in {% raw %} tags."""
        data = {
            "title": "Liquid Test",
            "date": "2025-01-01",
            "difficulty": "Easy",
            "content": "Test content",
            "link": "https://leetcode.com/problems/test",
            "question_id": "1",
            "ai_solutions": [
                {
                    "model": "gemini-3-flash-preview",
                    "generated_at": "2025-01-01 12:00:00",
                    "approach": "Test approach",
                    "solutions": {
                        "go": "package main\\nfunc main() {\\n    fmt.Println(\\\"{{}}\\\")\\n}"
                    },
                    "time_complexity": "O(1)",
                    "space_complexity": "O(1)"
                }
            ]
        }
        filepath = self.generator.generate_post(data)
        self.assertTrue(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for raw tags around the code
        self.assertIn('{% raw %}', content)
        self.assertIn('{% endraw %}', content)
        # The actual Go code should be present
        self.assertIn('fmt.Println', content)

    def test_partial_model_failure(self):
        """Test Case 2: Verify failed solution still renders correctly."""
        data = {
            "title": "Partial Failure Test",
            "date": "2025-01-02",
            "difficulty": "Medium",
            "content": "Test content",
            "link": "https://leetcode.com/problems/test-2",
            "question_id": "2",
            "ai_solutions": [
                {
                    "model": "gemini-3-flash-preview",
                    "generated_at": "2025-01-02 12:00:00",
                    "approach": "Failed to parse AI response",
                    "solutions": {
                        "python": "# Failed code"
                    },
                    "time_complexity": "N/A",
                    "space_complexity": "N/A"
                }
            ]
        }
        filepath = self.generator.generate_post(data)
        self.assertTrue(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Error message should show
        self.assertIn("Failed to parse AI response", content)

    def test_full_success_indentation(self):
        """Test Case 3: Verify full success and correct indentation."""
        data = {
            "title": "Indentation Test",
            "date": "2025-01-03",
            "difficulty": "Hard",
            "content": "Test content",
            "link": "https://leetcode.com/problems/test-3",
            "question_id": "3",
            "ai_solutions": [
                {
                    "model": "gemini-3-flash-preview",
                    "generated_at": "2025-01-03 12:00:00",
                    "approach": "Approach 1",
                    "solutions": {
                        "python": "    def test():\\n        return True"
                    },
                    "time_complexity": "O(1)",
                    "space_complexity": "O(1)"
                }
            ]
        }
        filepath = self.generator.generate_post(data)
        self.assertTrue(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check indentation for Gemini (should be dedented)
        self.assertIn("def test():", content)
        self.assertIn("return True", content)
        

    def test_raw_html_rendering(self):
        """Test Case 4: Verify HTML is rendered as-is with LeetCode styling."""
        html = "<p>We have two special characters:</p>\\n<ul>\\n<li>First character</li>\\n<li>Second character</li>\\n</ul>"
        
        data = {
            "title": "HTML Test",
            "date": "2025-01-04",
            "difficulty": "Easy",
            "content": html,
            "link": "https://leetcode.com/problems/html-test",
            "question_id": "4",
            "ai_solutions": []
        }
        
        filepath = self.generator.generate_post(data)
        self.assertTrue(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for LeetCode styling wrapper
        self.assertIn('class="leetcode-problem-description"', content)
        # Check that HTML is preserved
        self.assertIn("<ul>", content)
        self.assertIn("<li>First character</li>", content)
        self.assertIn("<li>Second character</li>", content)

if __name__ == '__main__':
    unittest.main()
