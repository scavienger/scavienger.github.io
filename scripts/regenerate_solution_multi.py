#!/usr/bin/env python3
"""
Regenerate AI Solutions for Existing Post with Multiple Models
Updates an existing blog post with solutions from multiple AI models
"""

import json
import os
import sys
import re
from datetime import datetime
from typing import List, Dict, Optional

# Import existing regenerator
from regenerate_solution import SolutionRegenerator


class MultiModelRegenerator:
    """Regenerates AI solutions using multiple models"""

    def __init__(self, posts_dir="_posts"):
        self.posts_dir = posts_dir

    def regenerate_with_models(self, date_str: str, model_names: List[str]) -> bool:
        """Regenerate solutions using multiple AI models"""

        # Create base regenerator
        base_regenerator = SolutionRegenerator(self.posts_dir)

        # Find post file
        print(f"Looking for post on {date_str}...", file=sys.stderr)
        filepath = base_regenerator.find_post_file(date_str)
        if not filepath:
            return False

        print(f"Found post: {filepath}", file=sys.stderr)

        # Read and parse post
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = base_regenerator.parse_frontmatter(content)
        if not frontmatter:
            return False

        # Extract LeetCode URL
        leetcode_url = frontmatter.get('leetcode_url', '')
        if not leetcode_url:
            print("No leetcode_url found in frontmatter", file=sys.stderr)
            return False

        print(f"LeetCode URL: {leetcode_url}", file=sys.stderr)

        # Extract title slug
        title_slug = base_regenerator.extract_title_slug(leetcode_url)
        if not title_slug:
            print("Failed to extract title slug from URL", file=sys.stderr)
            return False

        print(f"Title slug: {title_slug}", file=sys.stderr)

        # Fetch problem from LeetCode
        print(f"Fetching problem details from LeetCode...", file=sys.stderr)
        problem_data = base_regenerator.fetch_problem_by_slug(title_slug)
        if not problem_data:
            return False

        print(f"Problem: {problem_data['title']}", file=sys.stderr)

        # Generate problem section (once)
        print(f"Generating problem description section...", file=sys.stderr)
        new_problem_section = base_regenerator.generate_problem_section(problem_data)

        # Generate AI solutions for each model
        ai_solutions = []
        for model_name in model_names:
            print(f"\nGenerating AI solution with {model_name}...", file=sys.stderr)

            # Set environment for this model
            os.environ['AI_MODEL'] = model_name

            # Create regenerator with this model
            regenerator = SolutionRegenerator(self.posts_dir)

            # Generate solution
            ai_solution = regenerator.generate_ai_solution(problem_data)
            if ai_solution:
                ai_solution['model'] = model_name
                ai_solutions.append(ai_solution)
                print(f"✅ Solution generated with {model_name}", file=sys.stderr)
            else:
                print(f"❌ Failed to generate solution with {model_name}", file=sys.stderr)

        if not ai_solutions:
            print("No AI solutions were generated", file=sys.stderr)
            return False

        # Generate solution sections
        print(f"\nGenerating solution sections...", file=sys.stderr)
        solutions_section = self._generate_multi_solution_section(ai_solutions)

        # Reconstruct the post
        new_content = frontmatter_to_text(frontmatter) + '\n' + new_problem_section + '\n' + solutions_section

        # Write back
        print(f"Updating post file...", file=sys.stderr)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Successfully updated: {filepath}")
        print(f"   - Generated {len(ai_solutions)} AI solution(s)")
        return True

    def _generate_multi_solution_section(self, ai_solutions: List[Dict]) -> str:
        """Generate section with multiple AI solutions"""
        parts = []

        parts.append("## 🤖 AI-Generated Solutions\n")
        parts.append("We've generated solutions using multiple AI models. Click to expand each solution:\n")

        for idx, solution in enumerate(ai_solutions):
            model_name = solution.get('model', 'AI')

            # Model emoji mapping
            model_emojis = {
                'gemini-2.5-flash': '✨',
                'llama-3.3-70b-versatile': '⚡'
            }
            emoji = model_emojis.get(model_name, '🤖')

            # Create collapsible section
            is_first = idx == 0
            open_attr = ' open' if is_first else ''
            parts.append(f'\n<details{open_attr}>')
            parts.append(f'<summary><strong>{emoji} Solution from {model_name}</strong></summary>\n')

            # Approach
            parts.append("### Approach\n")
            parts.append(f"{solution.get('approach', 'No approach provided')}\n")

            # Code with multi-language tabs
            parts.append("### Code\n")
            solutions_code = solution.get('solutions', {})
            if solutions_code and isinstance(solutions_code, dict):
                # Use unique ID for each AI model's tabs
                parts.append(generate_code_tabs(solutions_code, suffix=f"-{model_name.replace('.', '-')}"))
            else:
                # Fallback
                code = solution.get('code', '# No code provided')
                parts.append("```python")
                parts.append(code)
                parts.append("```\n")

            # Complexity Analysis
            parts.append("### Complexity Analysis\n")
            parts.append(f"- **Time Complexity:** {solution.get('time_complexity', 'N/A')}\n")
            parts.append(f"- **Space Complexity:** {solution.get('space_complexity', 'N/A')}\n")

            parts.append('</details>\n')

        return '\n'.join(parts)


def frontmatter_to_text(frontmatter: Dict) -> str:
    """Convert frontmatter dict back to YAML text"""
    lines = ['---']
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        elif isinstance(value, str) and (':' in value or value.startswith('-')):
            lines.append(f'{key}: "{value}"')
        else:
            lines.append(f"{key}: {value}")
    lines.append('---')
    return '\n'.join(lines)


def generate_code_tabs(solutions: Dict, suffix: str = '') -> str:
    """Generate Pure CSS tabs for multi-language code"""
    # All 19 languages supported by LeetCode
    languages = [
        ('cpp', 'C++', 'cpp'),
        ('java', 'Java', 'java'),
        ('python', 'Python', 'python'),
        ('python3', 'Python3', 'python'),
        ('c', 'C', 'c'),
        ('csharp', 'C#', 'csharp'),
        ('javascript', 'JavaScript', 'javascript'),
        ('typescript', 'TypeScript', 'typescript'),
        ('php', 'PHP', 'php'),
        ('swift', 'Swift', 'swift'),
        ('kotlin', 'Kotlin', 'kotlin'),
        ('dart', 'Dart', 'dart'),
        ('go', 'Go', 'go'),
        ('ruby', 'Ruby', 'ruby'),
        ('scala', 'Scala', 'scala'),
        ('rust', 'Rust', 'rust'),
        ('racket', 'Racket', 'racket'),
        ('erlang', 'Erlang', 'erlang'),
        ('elixir', 'Elixir', 'elixir')
    ]

    tabs_html = ['<div class="code-tabs">\n']

    # Radio inputs with unique names and IDs
    radio_name = f"code-lang{suffix}"
    first_checked = False
    for lang_key, _, _ in languages:
        if lang_key in solutions:
            checked = ' checked' if not first_checked else ''
            first_checked = True
            tabs_html.append(f'  <input type="radio" name="{radio_name}" id="lang-{lang_key}{suffix}"{checked}>\n')

    # Tab labels
    tabs_html.append('  <div class="tab-labels">\n')
    for lang_key, lang_name, _ in languages:
        if lang_key in solutions:
            tabs_html.append(f'    <label for="lang-{lang_key}{suffix}">{lang_name}</label>\n')
    tabs_html.append('  </div>\n\n')

    # Tab panels
    for lang_key, _, fence in languages:
        if lang_key in solutions:
            code = solutions[lang_key].strip()
            tabs_html.append(f'  <div class="tab-panel" data-lang="{lang_key}">\n\n')
            tabs_html.append('{%% highlight %s %%}\n' % fence)
            tabs_html.append(code + '\n')
            tabs_html.append('{% endhighlight %}\n\n')
            tabs_html.append('  </div>\n\n')

    tabs_html.append('</div>\n')

    return ''.join(tabs_html)


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python regenerate_solution_multi.py <date> [models...]", file=sys.stderr)
        print("Example: python regenerate_solution_multi.py 2025-11-14 gemini-2.5-flash llama-3.3-70b-versatile", file=sys.stderr)
        return 1

    date_str = sys.argv[1]
    model_names = sys.argv[2:] if len(sys.argv) > 2 else ['gemini-2.5-flash', 'llama-3.3-70b-versatile']

    print(f"Regenerating solutions for date: {date_str}", file=sys.stderr)
    print(f"Using AI models: {', '.join(model_names)}", file=sys.stderr)

    regenerator = MultiModelRegenerator()
    success = regenerator.regenerate_with_models(date_str, model_names)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
