# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an automated LeetCode Daily Challenge blog powered by Jekyll and GitHub Pages. The system fetches daily LeetCode problems at 9:00 AM KST via GitHub Actions, generates AI solutions in 6 programming languages (Python, Java, C++, JavaScript, TypeScript, Go), and publishes them as blog posts.

## Key Commands

### Local Development

```bash
# Install Ruby dependencies
bundle install

# Serve the site locally (visit http://localhost:4000)
bundle exec jekyll serve

# Install Python dependencies
pip install -r scripts/requirements.txt
```

### Manual Post Generation

```bash
# Fetch today's LeetCode daily question
python scripts/fetch_leetcode.py > question_data.json

# Generate AI solution (requires API key in environment)
# AI_PROVIDER: 'gemini' or 'groq'
export AI_PROVIDER=gemini
export GEMINI_API_KEY="your-key"
python scripts/solve_with_ai.py question_data.json > question_with_solution.json

# Generate Jekyll post
python scripts/generate_post.py < question_with_solution.json
```

### Regenerate Solution for Existing Post

```bash
# Regenerate solution for a specific date
export GEMINI_API_KEY="your-key"
python scripts/regenerate_solution.py 2025-11-14 gemini

# Or use Groq
export GROQ_API_KEY="your-key"
python scripts/regenerate_solution.py 2025-11-14 groq
```

You can also trigger regeneration via GitHub Actions workflow "Regenerate AI Solution for Post" with date input (YYYY-MM-DD format).

## Architecture

### Automation Pipeline

The daily automation workflow (`.github/workflows/leetcode-daily.yml`) runs at 00:00 UTC (09:00 KST):

1. **fetch_leetcode.py**: Queries LeetCode GraphQL API for daily question
   - Fetches problem metadata (title, difficulty, topics, hints)
   - Converts HTML content to Markdown using BeautifulSoup and html2text
   - Handles tables by converting them to code blocks
   - Outputs JSON to stdout

2. **solve_with_ai.py**: Generates solutions using AI providers
   - Supports Gemini (gemini-2.5-flash) and Groq (llama-3.3-70b-versatile)
   - Prompts AI to return JSON with: approach, code for 6 languages, time/space complexity
   - Gracefully falls back if API key is missing (posts will have problem descriptions only)
   - Enhances question JSON with `ai_solution` field

3. **generate_post.py**: Creates Jekyll markdown post
   - Generates frontmatter with metadata (title, date, tags, difficulty, leetcode_url)
   - Builds post body with problem description, hints, and AI solution
   - Creates Pure CSS tabs for multi-language code display
   - Saves to `_posts/YYYY-MM-DD-title-slug.md`

### Post Structure

Generated posts follow this structure:
- **Frontmatter**: YAML with title, date, categories, tags, difficulty, leetcode_url
- **Problem Header**: Problem number, title, difficulty, topics
- **Problem Description**: Markdown-converted problem content
- **Illustrations**: Embedded images from problem (if any)
- **Hints**: Problem hints (if available)
- **AI Solution Section**:
  - Approach explanation
  - Multi-language code tabs (Pure CSS, no JavaScript)
  - Complexity analysis

### Multi-Language Code Tabs

The system uses Pure CSS tabs for code display (no JavaScript required):
- HTML structure in `_generate_code_tabs()` in generate_post.py
- CSS styling in `_sass/custom.scss` under `.code-tabs`
- Radio inputs control tab switching
- Supports 6 languages with language-specific syntax highlighting via Rouge

### Jekyll Configuration

- **Theme**: Minima (customized)
- **Markdown**: Kramdown with Rouge syntax highlighting
- **Timezone**: Asia/Seoul
- **Navigation**: Archive (by date), Difficulties (by level), Tags (by topic)
- **Custom SASS**: `_sass/custom.scss` (main styles), `_sass/dark-mode.scss` (dark theme)
- **Custom Layouts**: `_layouts/post.html` (with AdSense placeholders), `_layouts/home.html`

### AI Provider Configuration

The AI provider is set in workflow environment variable `AI_PROVIDER`:
- **Gemini** (default): Uses `GEMINI_API_KEY` secret, model `gemini-2.5-flash`
- **Groq**: Uses `GROQ_API_KEY` secret, model `llama-3.3-70b-versatile`
- Both offer free tiers
- Provider can be changed in `.github/workflows/leetcode-daily.yml` (line 48)

## Important Patterns

### Date Handling
- Posts use date format: `YYYY-MM-DD` (e.g., `2025-11-14`)
- Filenames: `_posts/YYYY-MM-DD-title-slug.md`
- Post frontmatter date: `YYYY-MM-DD 09:00:00 +0900` (KST timezone)

### JSON Data Flow
The scripts communicate via JSON piped through stdout:
1. `fetch_leetcode.py` → `question_data.json`
2. `solve_with_ai.py` → enhanced with `ai_solution` field → `question_with_solution.json`
3. `generate_post.py` → reads JSON from stdin, writes markdown file

### Error Handling
- Scripts use `try/except` with stderr logging
- AI solution generation has graceful fallback (posts without solutions if API fails)
- Workflows continue even if AI generation fails (`|| true` in step 52 of leetcode-daily.yml)

### HTML/Markdown Conversion
- `fetch_leetcode.py` handles conversion with special care for:
  - Tables → converted to code blocks (to avoid Jekyll rendering issues)
  - `<pre>` tags → triple backtick code blocks
  - Nested HTML → cleaned with html2text library

## File Naming and Organization

- **Posts**: `_posts/YYYY-MM-DD-{title-slug}.md` (automatically generated from title)
- **Scripts**: Executable Python scripts with shebang `#!/usr/bin/env python3`
- **Workflows**: `.github/workflows/leetcode-daily.yml` (daily), `regenerate-solution.yml` (manual)
- **Custom styles**: `_sass/` directory (imported by Minima theme)

## Development Workflow

This project uses a simplified Git Flow branching strategy:

### Branch Structure
- **`master`** (protected): Production/release branch, deployed to GitHub Pages
- **`develop`** (default): Main development branch, receives daily automated posts
- **`develop-feature-{name}-{id}`**: Individual feature branches

### Workflow
1. Create feature branch from `develop`: `git checkout -b develop-feature-{name}-{id}`
2. Make changes and commit
3. Push and create PR to `develop`
4. After review, merge to `develop`
5. Periodically merge `develop` → `master` via PR for releases

See **BRANCHING_STRATEGY.md** for detailed workflow instructions.

### Testing Changes
1. **Test scripts locally** before pushing to GitHub Actions
2. **Use test JSON data** to avoid hitting LeetCode API repeatedly
3. **Check CSS changes** with `bundle exec jekyll serve` locally
4. **Validate frontmatter** format (YAML must be valid)
5. **Test on develop** before releasing to master

## Key Constraints

- **LeetCode API**: Only provides "today's" daily question (no historical data via API)
- **Regeneration**: Uses `regenerate_solution.py` which re-fetches problem from LeetCode (works if problem is still accessible)
- **Pure CSS tabs**: No JavaScript dependency for code tabs (works with JS disabled)
- **Max zeros insight**: AI solutions leverage the mathematical insight that valid substrings have at most sqrt(N) zeros

## Dependencies

### Python (scripts/requirements.txt)
- `requests`: HTTP client for API calls
- `beautifulsoup4`: HTML parsing
- `html2text`: HTML to Markdown conversion
- `python-dateutil`: Date parsing
- `google-generativeai`: Gemini API client

### Ruby (Gemfile)
- `jekyll` (~> 4.3.0): Static site generator
- `minima` (~> 2.5): Jekyll theme
- `jekyll-feed`: RSS feed generation
- `jekyll-seo-tag`: SEO meta tags

## Testing Notes

- Posts are committed by `github-actions[bot]` user
- Manual workflow trigger available in Actions tab
- No changes committed if post already exists (duplicate prevention)
- Cleanup step removes temporary JSON files
