#!/usr/bin/env python3
"""
Generate Post by Date with Multiple AI Solutions
Creates a new post for a specified date with solutions from multiple AI models
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

# Import existing modules
from fetch_leetcode import LeetCodeFetcher
from solve_with_ai import AISolutionGenerator
from generate_post import PostGenerator


class MultiAIPostGenerator:
    """Generates posts with solutions from multiple AI models"""

    def __init__(self, posts_dir="_posts"):
        self.posts_dir = posts_dir
        self.fetcher = LeetCodeFetcher()

    def fetch_daily_question(self) -> Optional[Dict]:
        """Fetch today's daily question from LeetCode"""
        print("Fetching today's daily question from LeetCode...", file=sys.stderr)
        return self.fetcher.fetch_daily_question()

    def generate_solutions_for_models(self, problem_data: Dict, model_names: List[str]) -> List[Dict]:
        """Generate solutions using multiple AI models"""
        solutions = []

        for model_name in model_names:
            print(f"\nGenerating solution with {model_name}...", file=sys.stderr)

            # Set environment variable for the current model
            os.environ['AI_MODEL'] = model_name

            # Create new generator for this model
            generator = AISolutionGenerator()
            solution = generator.generate_solution(problem_data)

            if solution:
                solution['model'] = model_name
                solutions.append(solution)
                print(f"✅ Solution generated successfully with {model_name}", file=sys.stderr)
            else:
                print(f"❌ Failed to generate solution with {model_name}", file=sys.stderr)

        return solutions

    def generate_post(self, problem_data: Dict, date_str: str, ai_solutions: List[Dict]) -> Optional[str]:
        """Generate post with multiple AI solutions"""
        # Update date in problem data
        problem_data['date'] = date_str

        # Add all AI solutions to problem data
        problem_data['ai_solutions'] = ai_solutions

        # Use PostGenerator to create the file
        generator = PostGenerator(self.posts_dir)
        return generator.generate_post(problem_data)


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python generate_post_by_date.py <date> [models...]", file=sys.stderr)
        print("Example: python generate_post_by_date.py 2025-11-18 gemini-2.5-flash llama-3.3-70b-versatile", file=sys.stderr)
        return 1

    # Parse arguments
    date_str = sys.argv[1]
    model_names = sys.argv[2:] if len(sys.argv) > 2 else ['gemini-2.5-flash', 'llama-3.3-70b-versatile']

    # Validate date format
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"Invalid date format: {date_str}. Use YYYY-MM-DD", file=sys.stderr)
        return 1

    print(f"Generating post for date: {date_str}", file=sys.stderr)
    print(f"Using AI models: {', '.join(model_names)}", file=sys.stderr)

    # Create generator
    generator = MultiAIPostGenerator()

    # Fetch daily question
    problem_data = generator.fetch_daily_question()
    if not problem_data:
        print("Failed to fetch daily question", file=sys.stderr)
        return 1

    print(f"\nProblem: {problem_data['title']}", file=sys.stderr)
    print(f"Difficulty: {problem_data['difficulty']}", file=sys.stderr)

    # Generate solutions with multiple models
    ai_solutions = generator.generate_solutions_for_models(problem_data, model_names)

    if not ai_solutions:
        print("\n⚠️  No AI solutions were generated. Creating post with problem description only.", file=sys.stderr)

    # Generate post
    print(f"\nGenerating post file...", file=sys.stderr)
    filepath = generator.generate_post(problem_data, date_str, ai_solutions)

    if filepath:
        print(f"\n✅ Successfully created post: {filepath}")
        print(f"   - Problem: {problem_data['title']}")
        print(f"   - AI Solutions: {len(ai_solutions)}")
        return 0
    else:
        print("\n❌ Failed to generate post", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
