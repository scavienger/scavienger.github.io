#!/usr/bin/env python3
"""
Regenerate AI Solution for Existing Post
Updates an existing blog post with new AI-generated solutions
"""

import json
import os
import sys
import re
from datetime import datetime
from typing import Optional, Dict
import requests
from google import generativeai as genai
import html2text
from bs4 import BeautifulSoup


class SolutionRegenerator:
    """Regenerates AI solutions for existing posts"""

    GRAPHQL_URL = "https://leetcode.com/graphql"

    # GraphQL query to get problem by titleSlug
    PROBLEM_QUERY = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
            exampleTestcases
            topicTags {
                name
                slug
            }
            codeSnippets {
                lang
                langSlug
                code
            }
            hints
        }
    }
    """

    def __init__(self, posts_dir="_posts"):
        self.posts_dir = posts_dir
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Initialize AI provider
        self.provider = os.getenv('AI_PROVIDER', 'gemini').lower()
        self.gemini_model = None
        self.groq_api_key = None

        # Gemini setup
        gemini_key = os.getenv('GEMINI_API_KEY')
        if gemini_key:
            genai.configure(api_key=gemini_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.5-flash')

        # Groq setup
        self.groq_api_key = os.getenv('GROQ_API_KEY')

    def find_post_file(self, date_str: str) -> Optional[str]:
        """Find post file by date"""
        # List all files in _posts directory
        if not os.path.exists(self.posts_dir):
            print(f"Posts directory not found: {self.posts_dir}", file=sys.stderr)
            return None

        # Find file starting with the date
        for filename in os.listdir(self.posts_dir):
            if filename.startswith(date_str) and filename.endswith('.md'):
                return os.path.join(self.posts_dir, filename)

        print(f"No post found for date: {date_str}", file=sys.stderr)
        return None

    def parse_frontmatter(self, content: str) -> tuple:
        """Parse YAML frontmatter from post content"""
        # Extract frontmatter
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            print("Failed to parse frontmatter", file=sys.stderr)
            return None, content

        frontmatter_text = match.group(1)
        body = match.group(2)

        # Parse frontmatter (simple YAML parsing)
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')

        return frontmatter, body

    def extract_title_slug(self, leetcode_url: str) -> str:
        """Extract titleSlug from LeetCode URL"""
        # URL format: https://leetcode.com/problems/title-slug/
        match = re.search(r'/problems/([^/]+)', leetcode_url)
        if match:
            return match.group(1)
        return ""

    def fetch_problem_by_slug(self, title_slug: str) -> Optional[Dict]:
        """Fetch problem details from LeetCode by titleSlug"""
        try:
            response = self.session.post(
                self.GRAPHQL_URL,
                json={
                    'query': self.PROBLEM_QUERY,
                    'variables': {'titleSlug': title_slug}
                },
                timeout=10
            )
            response.raise_for_status()

            data = response.json()

            if 'errors' in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                return None

            question = data.get('data', {}).get('question')

            if not question:
                print(f"Question not found: {title_slug}", file=sys.stderr)
                return None

            return self._process_question(question)

        except Exception as e:
            print(f"Error fetching from LeetCode: {e}", file=sys.stderr)
            return None

    def _process_question(self, question: Dict) -> Dict:
        """Process question data"""
        # Get Python code snippet
        python_code = ""
        for snippet in question.get('codeSnippets', []):
            if snippet.get('langSlug') in ['python3', 'python']:
                python_code = snippet.get('code', '')
                break

        # Convert HTML content to Markdown
        html_content = question.get('content', '')
        markdown_content, images = self._convert_html_to_markdown(html_content)

        return {
            'title': question.get('title', 'Unknown Title'),
            'title_slug': question.get('titleSlug', ''),
            'question_id': question.get('questionFrontendId', ''),
            'difficulty': question.get('difficulty', 'Unknown'),
            'content': markdown_content,
            'images': images,
            'topics': [tag.get('name') for tag in question.get('topicTags', [])],
            'hints': question.get('hints', []),
            'code_template': python_code,
        }

    def _convert_html_to_markdown(self, html_content: str) -> tuple:
        """Convert HTML to Markdown"""
        if not html_content:
            return "", []

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract images
        images = []
        for img in soup.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', 'Problem Image')
            if src:
                images.append({'src': src, 'alt': alt})

        # Convert tables to code blocks
        # Process all tables at once to avoid issues with nested tables
        tables = soup.find_all('table')
        for table in tables:
            # Skip if table was already removed (e.g., nested table)
            if not table.parent:
                continue

            # Extract table content as plain text
            table_lines = []
            for row in table.find_all('tr'):
                cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                if cells:
                    # Format as simple text with spacing
                    table_lines.append('  '.join(cells))

            # Create a code block to replace the table
            if table_lines:
                code_block = soup.new_tag('pre')
                code_block.string = '\n'.join(table_lines)
                table.replace_with(code_block)

        # Convert <pre> tags to markdown code blocks (triple backticks)
        for pre in soup.find_all('pre'):
            pre_text = pre.get_text()
            # Replace <pre> with a marker that html2text won't mess up
            marker = soup.new_tag('p')
            marker.string = f"\n```\n{pre_text}\n```\n"
            pre.replace_with(marker)

        # Convert to markdown
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.skip_internal_links = False
        h.ignore_tables = True  # We already handled tables manually

        markdown = h.handle(str(soup))

        # Clean up
        while '\n\n\n' in markdown:
            markdown = markdown.replace('\n\n\n', '\n\n')

        return markdown.strip(), images

    def generate_ai_solution(self, problem_data: Dict) -> Optional[Dict]:
        """Generate AI solution using configured provider"""
        from solve_with_ai import AISolutionGenerator

        generator = AISolutionGenerator()
        generator.provider = self.provider

        # Override provider keys
        if self.gemini_model:
            generator.gemini_model = self.gemini_model
        if self.groq_api_key:
            generator.groq_api_key = self.groq_api_key

        return generator.generate_solution(problem_data)

    def generate_solution_section(self, ai_solution: Dict) -> str:
        """Generate the AI solution markdown section"""
        provider = self.provider.upper()
        provider_emojis = {
            'GEMINI': '✨',
            'GROQ': '⚡'
        }
        emoji = provider_emojis.get(provider, '🤖')

        parts = []
        parts.append(f"## {emoji} AI-Generated Solution ({provider})\n")

        # Approach
        parts.append("### Approach\n")
        parts.append(f"{ai_solution.get('approach', 'No approach provided')}\n")

        # Code with tabs
        parts.append("### Code\n")
        solutions = ai_solution.get('solutions', {})
        if solutions and isinstance(solutions, dict):
            parts.append(self._generate_code_tabs(solutions))
        else:
            # Fallback
            code = ai_solution.get('code', '# No code provided')
            parts.append("```python\n")
            parts.append(code + "\n")
            parts.append("```\n")

        # Complexity
        parts.append("\n### Complexity Analysis\n")
        parts.append(f"- **Time Complexity:** {ai_solution.get('time_complexity', 'N/A')}\n")
        parts.append(f"- **Space Complexity:** {ai_solution.get('space_complexity', 'N/A')}\n")

        return '\n'.join(parts)

    def _generate_code_tabs(self, solutions: Dict) -> str:
        """Generate Pure CSS tabs for code"""
        languages = [
            ('python', 'Python', 'python'),
            ('java', 'Java', 'java'),
            ('cpp', 'C++', 'cpp'),
            ('javascript', 'JavaScript', 'javascript'),
            ('typescript', 'TypeScript', 'typescript'),
            ('go', 'Go', 'go')
        ]

        tabs_html = ['<div class="code-tabs">\n']

        # Radio inputs
        for i, (lang_key, _, _) in enumerate(languages):
            if lang_key in solutions:
                checked = ' checked' if i == 0 else ''
                tabs_html.append(f'  <input type="radio" name="code-lang" id="lang-{lang_key}"{checked}>\n')

        # Tab labels
        tabs_html.append('  <div class="tab-labels">\n')
        for lang_key, lang_name, _ in languages:
            if lang_key in solutions:
                tabs_html.append(f'    <label for="lang-{lang_key}">{lang_name}</label>\n')
        tabs_html.append('  </div>\n\n')

        # Tab panels
        for lang_key, _, fence in languages:
            if lang_key in solutions:
                code = solutions[lang_key].strip()
                tabs_html.append(f'  <div class="tab-panel" data-lang="{lang_key}">\n\n')
                tabs_html.append(f'```{fence}\n')
                tabs_html.append(code + '\n')
                tabs_html.append('```\n\n')
                tabs_html.append('  </div>\n\n')

        tabs_html.append('</div>\n')

        return ''.join(tabs_html)

    def update_post(self, filepath: str, new_solution_section: str) -> bool:
        """Update post with new AI solution section"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find and replace AI solution section
            # Pattern: ## emoji AI-Generated Solution ... until next ## or end
            pattern = r'##\s*[^\n]*AI-Generated Solution[^\n]*\n.*?(?=\n##\s|\Z)'

            if re.search(pattern, content, re.DOTALL):
                # Replace existing solution
                new_content = re.sub(pattern, new_solution_section.rstrip(), content, flags=re.DOTALL)
                print("Replaced existing AI solution section", file=sys.stderr)
            else:
                # Append at the end
                new_content = content.rstrip() + '\n\n' + new_solution_section
                print("Appended new AI solution section", file=sys.stderr)

            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True

        except Exception as e:
            print(f"Error updating post: {e}", file=sys.stderr)
            return False


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python regenerate_solution.py <date> [provider]", file=sys.stderr)
        print("Example: python regenerate_solution.py 2025-11-14 gemini", file=sys.stderr)
        return 1

    date_str = sys.argv[1]
    provider = sys.argv[2] if len(sys.argv) > 2 else os.getenv('AI_PROVIDER', 'gemini')

    # Set provider
    os.environ['AI_PROVIDER'] = provider

    regenerator = SolutionRegenerator()

    # Find post file
    print(f"Looking for post on {date_str}...", file=sys.stderr)
    filepath = regenerator.find_post_file(date_str)
    if not filepath:
        return 1

    print(f"Found post: {filepath}", file=sys.stderr)

    # Read and parse post
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter, body = regenerator.parse_frontmatter(content)
    if not frontmatter:
        return 1

    # Extract LeetCode URL
    leetcode_url = frontmatter.get('leetcode_url', '')
    if not leetcode_url:
        print("No leetcode_url found in frontmatter", file=sys.stderr)
        return 1

    print(f"LeetCode URL: {leetcode_url}", file=sys.stderr)

    # Extract title slug
    title_slug = regenerator.extract_title_slug(leetcode_url)
    if not title_slug:
        print("Failed to extract title slug from URL", file=sys.stderr)
        return 1

    print(f"Title slug: {title_slug}", file=sys.stderr)

    # Fetch problem from LeetCode
    print(f"Fetching problem details from LeetCode...", file=sys.stderr)
    problem_data = regenerator.fetch_problem_by_slug(title_slug)
    if not problem_data:
        return 1

    print(f"Problem: {problem_data['title']}", file=sys.stderr)

    # Generate AI solution
    print(f"Generating AI solution with {provider}...", file=sys.stderr)
    ai_solution = regenerator.generate_ai_solution(problem_data)
    if not ai_solution:
        print("Failed to generate AI solution", file=sys.stderr)
        return 1

    print("AI solution generated successfully", file=sys.stderr)

    # Generate new solution section
    new_solution_section = regenerator.generate_solution_section(ai_solution)

    # Update post
    print(f"Updating post file...", file=sys.stderr)
    if regenerator.update_post(filepath, new_solution_section):
        print(f"✅ Successfully updated: {filepath}")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
