#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Solution Generator for LeetCode Problems
Supports Gemini (default) and Groq providers
"""

import json
import os
import sys
import textwrap
from typing import Dict, Optional
from datetime import datetime
import requests
from google import generativeai as genai

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    import os
    # Set encoding via environment variable (safer for subprocess)
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Only wrap if not already wrapped
    if hasattr(sys.stdout, 'buffer') and not isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'buffer') and not isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class AISolutionGenerator:
    """Generates solutions using AI providers"""

    # Model configurations
    MODEL_CONFIGS = {
        'gemini-2.5-flash': {
            'provider': 'gemini',
            'api_key_env': 'GEMINI_API_KEY'
        },
        'llama-3.3-70b-versatile': {
            'provider': 'groq',
            'api_key_env': 'GROQ_API_KEY'
        }
    }

    def __init__(self):
        # Get model name from environment (default: gemini-2.5-flash)
        self.model_name = os.getenv('AI_MODEL', 'gemini-2.5-flash')

        # Get model config
        model_config = self.MODEL_CONFIGS.get(self.model_name)
        if not model_config:
            print(f"Unknown model: {self.model_name}, falling back to gemini-2.5-flash", file=sys.stderr)
            self.model_name = 'gemini-2.5-flash'
            model_config = self.MODEL_CONFIGS['gemini-2.5-flash']

        self.provider = model_config['provider']

        # Initialize API clients based on available keys
        self.gemini_model = None
        self.groq_api_key = None

        # Gemini setup
        if self.provider == 'gemini':
            gemini_key = os.getenv('GEMINI_API_KEY')
            if gemini_key:
                genai.configure(api_key=gemini_key)
                self.gemini_model = genai.GenerativeModel(self.model_name)

        # Groq setup
        if self.provider == 'groq':
            self.groq_api_key = os.getenv('GROQ_API_KEY')

    def create_prompt(self, problem_data: Dict) -> str:
        """Create a prompt for the AI models"""
        title = problem_data.get('title', '')
        content = problem_data.get('content', '')
        difficulty = problem_data.get('difficulty', '')
        hints = problem_data.get('hints', [])
        code_template = problem_data.get('code_template', '')

        prompt = f"""You are an expert programmer solving LeetCode problems in multiple languages.

Problem: {title}
Difficulty: {difficulty}

Problem Description:
{content}

"""

        if hints:
            prompt += "Hints:\n"
            for i, hint in enumerate(hints, 1):
                prompt += f"{i}. {hint}\n"
            prompt += "\n"

        if code_template:
            prompt += f"Code Template (Python):\n```python\n{code_template}\n```\n\n"

        prompt += """Please provide solutions in ALL 19 programming languages supported by LeetCode: C++, Java, Python, Python3, C, C#, JavaScript, TypeScript, PHP, Swift, Kotlin, Dart, Go, Ruby, Scala, Rust, Racket, Erlang, and Elixir.

APPROACH REQUIREMENTS:
- Provide a DETAILED explanation of your approach (minimum 3-5 paragraphs)
- Explain the problem-solving strategy step by step
- Describe the algorithm logic clearly
- Include examples or edge cases if helpful
- Make the explanation thorough and educational

CODE FORMATTING REQUIREMENTS (CRITICAL):
- Each code solution MUST include proper line breaks and indentation
- DO NOT write code in a single line - use multiple lines with proper formatting
- Follow standard formatting conventions for each language
- Use newlines (\\n) to separate statements, function definitions, and control structures
- Properly indent nested blocks (loops, conditionals, functions)
- Add blank lines between logical sections for readability

COMPLEXITY ANALYSIS:
- Provide detailed time and space complexity with explanations
- Explain why the complexity is what it is

Format your response as JSON:
{
  "approach": "Detailed explanation here",
  "time_complexity": "O(...) with explanation",
  "space_complexity": "O(...) with explanation",
  "solutions": {
    "cpp": "Complete C++ code",
    "java": "Complete Java code",
    "python": "Complete Python code",
    "python3": "Complete Python3 code",
    "c": "Complete C code",
    "csharp": "Complete C# code",
    "javascript": "Complete JavaScript code",
    "typescript": "Complete TypeScript code",
    "php": "Complete PHP code",
    "swift": "Complete Swift code",
    "kotlin": "Complete Kotlin code",
    "dart": "Complete Dart code",
    "go": "Complete Go code",
    "ruby": "Complete Ruby code",
    "scala": "Complete Scala code",
    "rust": "Complete Rust code",
    "racket": "Complete Racket code",
    "erlang": "Complete Erlang code",
    "elixir": "Complete Elixir code"
  }
}

Important: Each code solution must be complete and runnable. Include class/function definitions, imports, and follow language conventions for each specific language.

Provide ONLY the JSON response, no additional text."""

        return prompt

    def _clean_code(self, code: str) -> str:
        """Clean code by removing markdown code block markers and normalizing whitespace"""
        if not code:
            return code

        # Remove markdown code block markers (```python, ```cpp, etc.)
        lines = code.split('\n')
        cleaned_lines = []

        for line in lines:
            stripped = line.strip()
            # Skip lines that are just code block markers
            if stripped.startswith('```') and len(stripped) <= 20:
                continue
            cleaned_lines.append(line)

        # Rejoin and clean up
        cleaned = '\n'.join(cleaned_lines)

        # Remove leading/trailing whitespace
        cleaned = cleaned.strip()

        # Remove common leading indentation from all lines (fixes Llama extra indentation)
        cleaned = textwrap.dedent(cleaned)

        return cleaned

    def parse_json_response(self, response_text: str) -> Dict:
        """Extract and parse JSON from AI response"""
        try:
            # Find JSON in the response
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                json_str = response_text[start:end]
                parsed = json.loads(json_str)

                # Validate that we have the expected structure
                if 'solutions' in parsed and isinstance(parsed['solutions'], dict):
                    # Clean all code solutions
                    for lang, code in parsed['solutions'].items():
                        parsed['solutions'][lang] = self._clean_code(code)
                    return parsed
                # Fallback for old format (single language)
                elif 'code' in parsed:
                    return {
                        "approach": parsed.get("approach", "N/A"),
                        "time_complexity": parsed.get("time_complexity", "N/A"),
                        "space_complexity": parsed.get("space_complexity", "N/A"),
                        "solutions": {
                            "python": self._clean_code(parsed.get("code", ""))
                        }
                    }
                else:
                    return self._create_error_response(response_text)
            else:
                return self._create_error_response(response_text)
        except json.JSONDecodeError:
            return self._create_error_response(response_text)

    def _create_error_response(self, response_text: str) -> Dict:
        """Create a fallback response when parsing fails"""
        return {
            "approach": "Failed to parse AI response",
            "time_complexity": "N/A",
            "space_complexity": "N/A",
            "solutions": {
                "python": f"# Failed to parse response\n# Raw output:\n{response_text[:500]}"
            }
        }

    def solve_with_gemini(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Gemini"""
        if not self.gemini_model:
            print("Gemini API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)
            response = self.gemini_model.generate_content(prompt)
            return self.parse_json_response(response.text)
        except Exception as e:
            print(f"Error with Gemini: {e}", file=sys.stderr)
            return None

    def solve_with_groq(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Groq"""
        if not self.groq_api_key:
            print("Groq API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)

            # Call Groq API (OpenAI-compatible endpoint)
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.groq_api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model_name,
                    "messages": [
                        {"role": "system", "content": "You are an expert programmer solving LeetCode problems. Always format code with proper line breaks and indentation."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 8000,
                    "response_format": {"type": "json_object"}
                },
                timeout=60
            )
            response.raise_for_status()

            data = response.json()
            content = data['choices'][0]['message']['content']
            return self.parse_json_response(content)

        except Exception as e:
            print(f"Error with Groq: {e}", file=sys.stderr)
            return None

    def generate_solution(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using the configured model"""
        print(f"Generating solution with {self.model_name}...", file=sys.stderr)

        if self.provider == 'groq':
            return self.solve_with_groq(problem_data)
        elif self.provider == 'gemini':
            return self.solve_with_gemini(problem_data)
        else:
            print(f"Unknown provider: {self.provider}, falling back to Gemini", file=sys.stderr)
            return self.solve_with_gemini(problem_data)


def main():
    """Main function"""
    if len(sys.argv) > 1:
        # Read from file if provided
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            problem_data = json.load(f)
    else:
        # Read from stdin
        problem_data = json.load(sys.stdin)

    generator = AISolutionGenerator()
    solution = generator.generate_solution(problem_data)

    if solution:
        # Add solution to problem data with timestamp
        problem_data['ai_solution'] = {
            'model': generator.model_name,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S %z'),
            **solution
        }
    else:
        print("Failed to generate solution", file=sys.stderr)

    # Output enhanced problem data as JSON
    print(json.dumps(problem_data, indent=2, ensure_ascii=False))

    return 0 if solution else 1


if __name__ == "__main__":
    sys.exit(main())
