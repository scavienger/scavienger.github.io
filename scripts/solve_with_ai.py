#!/usr/bin/env python3
"""
AI Solution Generator for LeetCode Problems
Supports multiple AI providers with Gemini as default
"""

import json
import os
import sys
from typing import Dict, Optional
import openai
from google import generativeai as genai


class AISolutionGenerator:
    """Generates solutions using AI providers"""

    def __init__(self):
        # Get provider from environment (default: gemini)
        self.provider = os.getenv('AI_PROVIDER', 'gemini').lower()

        # Initialize API clients based on available keys
        self.gemini_model = None
        self.openai_client = None
        self.groq_client = None

        # Gemini setup
        gemini_key = os.getenv('GEMINI_API_KEY')
        if gemini_key:
            genai.configure(api_key=gemini_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # OpenAI setup
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key:
            self.openai_client = openai.OpenAI(api_key=openai_key)

        # Groq setup (OpenAI-compatible)
        groq_key = os.getenv('GROQ_API_KEY')
        if groq_key:
            self.groq_client = openai.OpenAI(
                api_key=groq_key,
                base_url="https://api.groq.com/openai/v1"
            )

    def create_prompt(self, problem_data: Dict) -> str:
        """Create a prompt for the AI models"""
        title = problem_data.get('title', '')
        content = problem_data.get('content', '')
        difficulty = problem_data.get('difficulty', '')
        hints = problem_data.get('hints', [])
        code_template = problem_data.get('code_template', '')

        prompt = f"""You are an expert Python programmer solving LeetCode problems.

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
            prompt += f"Code Template:\n```python\n{code_template}\n```\n\n"

        prompt += """Please provide:
1. A clear explanation of your approach
2. Complete Python solution code
3. Time complexity analysis
4. Space complexity analysis

Format your response as JSON with the following structure:
{
  "approach": "Your explanation here",
  "code": "Complete Python code here",
  "time_complexity": "O(...) explanation",
  "space_complexity": "O(...) explanation"
}

Provide ONLY the JSON response, no additional text."""

        return prompt

    def parse_json_response(self, response_text: str) -> Dict:
        """Extract and parse JSON from AI response"""
        try:
            # Find JSON in the response
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                json_str = response_text[start:end]
                return json.loads(json_str)
            else:
                return {
                    "approach": "Failed to parse structured response",
                    "code": response_text,
                    "time_complexity": "N/A",
                    "space_complexity": "N/A"
                }
        except json.JSONDecodeError:
            return {
                "approach": "Failed to parse JSON response",
                "code": response_text,
                "time_complexity": "N/A",
                "space_complexity": "N/A"
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

    def solve_with_openai(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using OpenAI GPT-4"""
        if not self.openai_client:
            print("OpenAI API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert Python programmer solving LeetCode problems."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4096
            )
            return self.parse_json_response(response.choices[0].message.content)
        except Exception as e:
            print(f"Error with OpenAI: {e}", file=sys.stderr)
            return None

    def solve_with_groq(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Groq"""
        if not self.groq_client:
            print("Groq API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an expert Python programmer solving LeetCode problems."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4096
            )
            return self.parse_json_response(response.choices[0].message.content)
        except Exception as e:
            print(f"Error with Groq: {e}", file=sys.stderr)
            return None

    def generate_solution(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using the configured provider"""
        print(f"Generating solution with {self.provider}...", file=sys.stderr)

        if self.provider == 'gemini':
            return self.solve_with_gemini(problem_data)
        elif self.provider == 'groq':
            return self.solve_with_groq(problem_data)
        elif self.provider in ['openai', 'gpt4']:
            return self.solve_with_openai(problem_data)
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
        # Add solution to problem data
        problem_data['ai_solution'] = {
            'provider': generator.provider,
            **solution
        }
    else:
        print("Failed to generate solution", file=sys.stderr)

    # Output enhanced problem data as JSON
    print(json.dumps(problem_data, indent=2, ensure_ascii=False))

    return 0 if solution else 1


if __name__ == "__main__":
    sys.exit(main())
