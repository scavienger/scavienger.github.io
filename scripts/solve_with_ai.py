#!/usr/bin/env python3
"""
AI Solution Generator for LeetCode Problems
Uses Claude, GPT-4, and Gemini to generate multiple solutions
"""

import json
import os
import sys
from typing import Dict, Optional
import anthropic
import openai
from google import generativeai as genai


class AISolutionGenerator:
    """Generates solutions using multiple AI models"""

    def __init__(self):
        # Initialize API clients
        self.anthropic_client = None
        self.openai_client = None
        self.gemini_model = None

        # Get API keys from environment
        anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        openai_key = os.getenv('OPENAI_API_KEY')
        gemini_key = os.getenv('GEMINI_API_KEY')

        # Initialize clients if keys are available
        if anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=anthropic_key)

        if openai_key:
            self.openai_client = openai.OpenAI(api_key=openai_key)

        if gemini_key:
            genai.configure(api_key=gemini_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')

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

    def solve_with_claude(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Claude"""
        if not self.anthropic_client:
            print("Claude API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)

            message = self.anthropic_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # Try to parse JSON from response
            try:
                # Find JSON in the response
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = response_text[start:end]
                    solution = json.loads(json_str)
                    return solution
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

        except Exception as e:
            print(f"Error with Claude: {e}", file=sys.stderr)
            return None

    def solve_with_gpt4(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using GPT-4"""
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

            response_text = response.choices[0].message.content

            # Try to parse JSON from response
            try:
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = response_text[start:end]
                    solution = json.loads(json_str)
                    return solution
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

        except Exception as e:
            print(f"Error with GPT-4: {e}", file=sys.stderr)
            return None

    def solve_with_gemini(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Gemini"""
        if not self.gemini_model:
            print("Gemini API key not found", file=sys.stderr)
            return None

        try:
            prompt = self.create_prompt(problem_data)

            response = self.gemini_model.generate_content(prompt)
            response_text = response.text

            # Try to parse JSON from response
            try:
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = response_text[start:end]
                    solution = json.loads(json_str)
                    return solution
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

        except Exception as e:
            print(f"Error with Gemini: {e}", file=sys.stderr)
            return None

    def generate_all_solutions(self, problem_data: Dict) -> Dict:
        """Generate solutions from all available AI models"""
        solutions = {}

        print("Generating solution with Claude...", file=sys.stderr)
        claude_solution = self.solve_with_claude(problem_data)
        if claude_solution:
            solutions['claude'] = claude_solution

        print("Generating solution with GPT-4...", file=sys.stderr)
        gpt4_solution = self.solve_with_gpt4(problem_data)
        if gpt4_solution:
            solutions['gpt4'] = gpt4_solution

        print("Generating solution with Gemini...", file=sys.stderr)
        gemini_solution = self.solve_with_gemini(problem_data)
        if gemini_solution:
            solutions['gemini'] = gemini_solution

        return solutions


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
    solutions = generator.generate_all_solutions(problem_data)

    # Add solutions to problem data
    problem_data['ai_solutions'] = solutions

    # Output enhanced problem data as JSON
    print(json.dumps(problem_data, indent=2, ensure_ascii=False))

    return 0 if solutions else 1


if __name__ == "__main__":
    sys.exit(main())
