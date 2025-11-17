#!/usr/bin/env python3
"""
Jekyll Post Generator for LeetCode Daily Question
Generates a markdown post from LeetCode question data
"""

import json
import sys
import os
import re
from datetime import datetime
from dateutil import parser as date_parser


class PostGenerator:
    """Generates Jekyll markdown posts"""

    def __init__(self, posts_dir="_posts"):
        self.posts_dir = posts_dir

    def generate_post(self, question_data):
        """Generate a Jekyll post from question data"""
        try:
            # Parse date
            question_date = date_parser.parse(question_data['date'])
            date_str = question_date.strftime('%Y-%m-%d')

            # Create filename-safe title
            safe_title = self._sanitize_filename(question_data['title'])
            filename = f"{date_str}-{safe_title}.md"
            filepath = os.path.join(self.posts_dir, filename)

            # Ensure posts directory exists
            os.makedirs(self.posts_dir, exist_ok=True)

            # Generate post content
            content = self._generate_content(question_data, date_str)

            # Write post
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Post generated: {filepath}")
            return filepath

        except Exception as e:
            print(f"Error generating post: {e}", file=sys.stderr)
            return None

    def _sanitize_filename(self, title):
        """Convert title to filename-safe format"""
        # Remove special characters and convert to lowercase
        safe = re.sub(r'[^\w\s-]', '', title.lower())
        # Replace spaces with hyphens
        safe = re.sub(r'[\s_]+', '-', safe)
        # Remove leading/trailing hyphens
        safe = safe.strip('-')
        return safe

    def _clean_html_content(self, html_content):
        """Clean HTML content for markdown"""
        # Basic HTML to markdown conversion
        # Remove HTML tags but keep content
        content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html_content)
        content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)
        content = re.sub(r'<code>(.*?)</code>', r'`\1`', content)
        content = re.sub(r'<pre>(.*?)</pre>', r'```\n\1\n```', content, flags=re.DOTALL)
        content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
        content = re.sub(r'<ul>', '\n', content)
        content = re.sub(r'</ul>', '\n', content)
        content = re.sub(r'<li>(.*?)</li>', r'- \1', content)
        content = re.sub(r'<sup>(.*?)</sup>', r'^\1', content)
        content = re.sub(r'<sub>(.*?)</sub>', r'_\1', content)
        content = re.sub(r'&nbsp;', ' ', content)
        content = re.sub(r'&lt;', '<', content)
        content = re.sub(r'&gt;', '>', content)
        content = re.sub(r'&amp;', '&', content)
        content = re.sub(r'&quot;', '"', content)

        # Remove any remaining HTML tags
        content = re.sub(r'<[^>]+>', '', content)

        return content.strip()

    def _generate_code_tabs(self, solutions, suffix=''):
        """Generate Pure CSS tabs for multi-language code

        Args:
            solutions: Dictionary of language code solutions
            suffix: Optional suffix for unique IDs when multiple tab sets exist
        """
        # Language configurations: (key, display name, code fence)
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

        # Start the tabs container
        tabs_html = ['<div class="code-tabs">\n']

        # Create radio inputs (hidden) with unique names and IDs
        radio_name = f"code-lang{suffix}"
        first_checked = False
        for i, (lang_key, _, _) in enumerate(languages):
            if lang_key in solutions:
                checked = ' checked' if not first_checked else ''
                first_checked = True
                tabs_html.append(f'  <input type="radio" name="{radio_name}" id="lang-{lang_key}{suffix}"{checked}>\n')

        # Create tab labels
        tabs_html.append('  <div class="tab-labels">\n')
        for lang_key, lang_name, _ in languages:
            if lang_key in solutions:
                tabs_html.append(f'    <label for="lang-{lang_key}{suffix}">{lang_name}</label>\n')
        tabs_html.append('  </div>\n\n')

        # Create tab content panels
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

    def _generate_content(self, question_data, date_str):
        """Generate the markdown content"""
        title = question_data['title']
        difficulty = question_data['difficulty']
        # Content is now in markdown format from fetch_leetcode.py
        content = question_data.get('content', '')
        images = question_data.get('images', [])
        topics = question_data.get('topics', [])
        hints = question_data.get('hints', [])
        code_template = question_data.get('code_template', '')
        leetcode_url = question_data['link']
        question_id = question_data.get('question_id', '')

        # Build frontmatter
        frontmatter = f"""---
layout: post
title: "{title}"
date: {date_str} 09:00:00 +0900
categories: [LeetCode, {difficulty}]
tags: {json.dumps(topics, ensure_ascii=False)}
difficulty: {difficulty}
leetcode_url: {leetcode_url}
---
"""

        # Build post body
        body_parts = []

        # Problem header
        body_parts.append(f"## Problem #{question_id}: {title}\n")
        body_parts.append(f"**Difficulty:** {difficulty}\n")

        if topics:
            body_parts.append(f"**Topics:** {', '.join(topics)}\n")

        # Problem description
        body_parts.append("## Problem Description\n")
        body_parts.append(content + "\n")

        # Add images if any
        if images:
            body_parts.append("### Illustrations\n")
            for img in images:
                src = img.get('src', '')
                alt = img.get('alt', 'Problem Image')
                body_parts.append(f"![{alt}]({src})\n")

        # Hints section
        if hints:
            body_parts.append("## Hints\n")
            for i, hint in enumerate(hints, 1):
                cleaned_hint = self._clean_html_content(hint)
                body_parts.append(f"{i}. {cleaned_hint}\n")

        # AI Solution section - support both single and multiple solutions
        ai_solution = question_data.get('ai_solution', {})
        ai_solutions = question_data.get('ai_solutions', [])

        # Handle both old format (single solution) and new format (multiple solutions)
        if ai_solutions:
            # New format: multiple AI solutions
            body_parts.append("## 🤖 AI-Generated Solutions\n")
            body_parts.append("We've generated solutions using multiple AI models. Click to expand each solution:\n")

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
                body_parts.append(f'\n<details{open_attr}>')
                body_parts.append(f'<summary><strong>{emoji} Solution from {model_name}</strong></summary>\n')

                # Approach
                body_parts.append("### Approach\n")
                body_parts.append(f"{solution.get('approach', 'No approach provided')}\n")

                # Code with multi-language tabs
                body_parts.append("### Code\n")
                solutions_code = solution.get('solutions', {})
                if solutions_code and isinstance(solutions_code, dict):
                    # Use unique ID for each AI model's tabs
                    body_parts.append(self._generate_code_tabs(solutions_code, suffix=f"-{model_name.replace('.', '-')}"))
                else:
                    # Fallback
                    code = solution.get('code', '# No code provided')
                    body_parts.append("```python")
                    body_parts.append(code)
                    body_parts.append("```\n")

                # Complexity Analysis
                body_parts.append("### Complexity Analysis\n")
                body_parts.append(f"- **Time Complexity:** {solution.get('time_complexity', 'N/A')}\n")
                body_parts.append(f"- **Space Complexity:** {solution.get('space_complexity', 'N/A')}\n")

                body_parts.append('</details>\n')

        elif ai_solution:
            # Old format: single AI solution
            # Get model name (new format) or fallback to provider (old format)
            model_name = ai_solution.get('model')
            if not model_name:
                # Fallback for old format
                provider = ai_solution.get('provider', 'AI').upper()
                model_name = {
                    'GEMINI': 'gemini-2.5-flash',
                    'GROQ': 'llama-3.3-70b-versatile'
                }.get(provider, 'AI')

            # Model emoji mapping
            model_emojis = {
                'gemini-2.5-flash': '✨',
                'llama-3.3-70b-versatile': '⚡'
            }
            emoji = model_emojis.get(model_name, '🤖')

            body_parts.append(f"## {emoji} AI-Generated Solution ({model_name})\n")

            # Approach
            body_parts.append("### Approach\n")
            body_parts.append(f"{ai_solution.get('approach', 'No approach provided')}\n")

            # Code with multi-language tabs
            body_parts.append("### Code\n")
            solutions = ai_solution.get('solutions', {})
            if solutions and isinstance(solutions, dict):
                # Generate Pure CSS tabs for multiple languages
                body_parts.append(self._generate_code_tabs(solutions))
            else:
                # Fallback for old format (single Python code)
                code = ai_solution.get('code', '# No code provided')
                body_parts.append("```python")
                body_parts.append(code)
                body_parts.append("```\n")

            # Complexity Analysis
            body_parts.append("### Complexity Analysis\n")
            body_parts.append(f"- **Time Complexity:** {ai_solution.get('time_complexity', 'N/A')}")
            body_parts.append(f"- **Space Complexity:** {ai_solution.get('space_complexity', 'N/A')}\n")
        else:
            # Fallback: manual solution template
            body_parts.append("## Solution\n")
            body_parts.append("### Approach\n")
            body_parts.append("TODO: Add solution approach here.\n")

            body_parts.append("### Code\n")
            body_parts.append("```python")
            if code_template:
                body_parts.append(code_template)
            else:
                body_parts.append("# Solution code here")
            body_parts.append("```\n")

            # Complexity analysis
            body_parts.append("### Complexity Analysis\n")
            body_parts.append("- **Time Complexity:** O(?)\n")
            body_parts.append("- **Space Complexity:** O(?)\n")

        return frontmatter + "\n" + "\n".join(body_parts)


def main():
    """Main function"""
    if len(sys.argv) > 1:
        # Read from file if provided
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            question_data = json.load(f)
    else:
        # Read from stdin
        question_data = json.load(sys.stdin)

    generator = PostGenerator()
    result = generator.generate_post(question_data)

    if result:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
