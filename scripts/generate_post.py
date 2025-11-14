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

    def _generate_content(self, question_data, date_str):
        """Generate the markdown content"""
        title = question_data['title']
        difficulty = question_data['difficulty']
        content = self._clean_html_content(question_data['content'])
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

        # Hints section
        if hints:
            body_parts.append("## Hints\n")
            for i, hint in enumerate(hints, 1):
                cleaned_hint = self._clean_html_content(hint)
                body_parts.append(f"{i}. {cleaned_hint}\n")

        # AI Solution section
        ai_solution = question_data.get('ai_solution', {})

        if ai_solution:
            provider = ai_solution.get('provider', 'AI').upper()

            # Provider emoji mapping
            provider_emojis = {
                'GEMINI': '✨',
                'GROQ': '⚡'
            }
            emoji = provider_emojis.get(provider, '🤖')

            body_parts.append(f"## {emoji} AI-Generated Solution ({provider})\n")

            # Approach
            body_parts.append("### Approach\n")
            body_parts.append(f"{ai_solution.get('approach', 'No approach provided')}\n")

            # Code
            body_parts.append("### Code\n")
            body_parts.append("```python")
            body_parts.append(ai_solution.get('code', '# No code provided'))
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
