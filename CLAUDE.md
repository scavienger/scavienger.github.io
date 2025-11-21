# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an automated LeetCode Daily Challenge blog powered by Jekyll and GitHub Pages. The system fetches daily LeetCode problems at 9:00 AM KST via GitHub Actions, generates AI solutions in 19 programming languages using multiple AI models (Gemini and Llama), and publishes them as interactive blog posts with modern features like dark mode, table of contents, and multi-language code tabs.

## Key Features

### User Interface
- **Dark Mode**: System preference detection with manual toggle, localStorage persistence, and anti-flash loading
- **Table of Contents**: Auto-generated from headings with scroll-spy, collapsible on mobile, smart sticky behavior
- **Code Tabs**: JavaScript-enhanced tabs with dropdown for 19+ languages, user preference persistence
- **Multiple AI Solutions**: Collapsible sections showing solutions from different AI models (Gemini ✨ and Llama ⚡)
- **Modern Design**: Hero section, statistics dashboard, card-based layout, breadcrumb navigation
- **Related Posts**: Automatic suggestions based on difficulty level
- **Responsive**: Mobile-first design with accessibility features

### Programming Languages

**Primary Languages** (shown as tabs):
1. Python
2. Java
3. C++
4. JavaScript
5. TypeScript
6. Go

**Secondary Languages** (in dropdown menu):
7. Python3
8. C
9. C#
10. PHP
11. Swift
12. Kotlin
13. Dart
14. Ruby
15. Scala
16. Rust
17. Racket
18. Erlang
19. Elixir

### AI Models
- **Gemini 2.5 Flash** (Google, emoji: ✨): Fast, efficient, good at code generation
- **Llama 3.3 70B** (Groq, emoji: ⚡): Powerful open-source model, detailed explanations

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

# Generate AI solution with single model
export AI_MODEL=gemini  # or 'groq'
export GEMINI_API_KEY="your-key"
python scripts/solve_with_ai.py question_data.json > question_with_solution.json

# Generate Jekyll post
python scripts/generate_post.py < question_with_solution.json

# Generate post for specific date with multiple AI models
export GEMINI_API_KEY="your-key"
export GROQ_API_KEY="your-key"
python scripts/generate_post_by_date.py 2025-11-18 gemini groq
```

### Regenerate Solutions

```bash
# Regenerate with single model
export GEMINI_API_KEY="your-key"
python scripts/regenerate_solution.py 2025-11-14 gemini

# Regenerate with multiple models (creates collapsible sections)
export GEMINI_API_KEY="your-key"
export GROQ_API_KEY="your-key"
python scripts/regenerate_solution_multi.py 2025-11-14 gemini groq

# Batch regenerate multiple posts
python scripts/batch_regenerate.py 2025-11-01 2025-11-10 gemini
```

You can also trigger regeneration via GitHub Actions:
- **"Regenerate AI Solution for Post"**: Single date, choice of single model or both
- **"Generate Post by Date"**: Generate post for specific date with multiple models

### JavaScript Development

The project uses vanilla JavaScript (no build process) for:
- **Dark mode**: `assets/js/dark-mode.js`
- **Code tabs**: `assets/js/code-tabs.js`

No compilation needed - changes are immediately reflected when you refresh the page.

## Architecture

### Directory Structure

```
scavienger.github.io/
├── .github/workflows/           # GitHub Actions
│   ├── leetcode-daily.yml      # Daily automation (00:00 UTC)
│   ├── regenerate-solution.yml # Manual regeneration workflow
│   └── generate-post-by-date.yml # Generate by specific date
├── _includes/                   # Jekyll includes
│   ├── custom-head.html        # Scripts, meta tags, AdSense
│   ├── dark-mode-toggle.html   # Floating dark mode button
│   └── toc.html                # Table of contents component
├── _layouts/                    # Jekyll layouts
│   ├── home.html               # Homepage with hero and stats
│   └── post.html               # Post layout with TOC and related posts
├── _posts/                      # Generated blog posts
├── _sass/                       # SCSS stylesheets
│   ├── custom.scss             # Main styles (1602 lines)
│   └── dark-mode.scss          # Dark mode theme overrides
├── assets/js/                   # JavaScript files
│   ├── dark-mode.js            # Dark mode toggle logic
│   └── code-tabs.js            # Code tab interactions
├── scripts/                     # Python automation
│   ├── fetch_leetcode.py       # Fetch daily question from LeetCode API
│   ├── solve_with_ai.py        # Generate solution with AI model
│   ├── generate_post.py        # Create Jekyll markdown post
│   ├── regenerate_solution.py  # Regenerate single solution
│   ├── regenerate_solution_multi.py # Regenerate with multiple models
│   ├── generate_post_by_date.py # Generate post for specific date
│   ├── batch_regenerate.py     # Batch regenerate multiple posts
│   └── requirements.txt        # Python dependencies
├── _config.yml                  # Jekyll configuration
├── Gemfile                      # Ruby dependencies
└── CLAUDE.md                    # This file
```

### Automation Pipeline

The daily automation workflow (`.github/workflows/leetcode-daily.yml`) runs at 00:00 UTC (09:00 KST):

1. **fetch_leetcode.py**: Queries LeetCode GraphQL API
   - Fetches problem metadata (title, difficulty, topics, hints, examples)
   - Converts HTML content to Markdown using BeautifulSoup and html2text
   - Handles tables by converting to code blocks (prevents Jekyll rendering issues)
   - Extracts images and embeds them in markdown
   - Outputs JSON to stdout

2. **solve_with_ai.py**: Generates AI solution
   - Supports two models: `gemini-2.5-flash` or `llama-3.3-70b-versatile`
   - Model selected via `AI_MODEL` environment variable
   - Prompts AI with strict JSON format requirements:
     - `approach`: 3-5 paragraph explanation
     - `code`: Solutions in all 19 languages
     - `time_complexity`: Big O with explanation
     - `space_complexity`: Big O with explanation
   - Validates JSON response and extracts solution
   - Gracefully falls back if API key missing (posts without solutions)
   - Enhances question JSON with `ai_solution` field

3. **generate_post.py**: Creates Jekyll markdown post
   - Generates YAML frontmatter (title, date, tags, difficulty, leetcode_url)
   - Builds problem description with examples and constraints
   - Creates collapsible `<details>` sections for multiple AI solutions
   - Generates code tabs with unique IDs for each solution
   - Outputs to `_posts/YYYY-MM-DD-title-slug.md`

### Post Structure

Generated posts follow this structure:

```markdown
---
layout: post
title: "Problem Title"
date: YYYY-MM-DD 09:00:00 +0900
categories: [LeetCode, Daily Challenge]
tags: [topic1, topic2, ...]
difficulty: Easy/Medium/Hard
leetcode_url: https://leetcode.com/problems/...
---

## Problem Description
[Markdown-converted problem content]

## Examples
[Example inputs/outputs]

## Constraints
[Problem constraints]

## Hints
[LeetCode hints if available]

## AI Solutions

<details open>
<summary>✨ Solution by Gemini</summary>

### Approach
[3-5 paragraph explanation]

[Code tabs for 19 languages]

### Complexity Analysis
- **Time Complexity**: O(...)
- **Space Complexity**: O(...)
</details>

<details>
<summary>⚡ Solution by Llama</summary>
[Similar structure]
</details>
```

### Code Tab System

The code tabs use a hybrid approach:
- **Pure CSS** for basic tab switching (no JavaScript required)
- **JavaScript enhancement** for:
  - Dropdown menu for secondary languages
  - User language preference persistence (localStorage)
  - Click-outside-to-close dropdown
  - Automatic language selection on page load

**Implementation Details:**
- Radio inputs control tab switching (`name="code-tabs-{suffix}"`)
- Each AI solution gets unique suffix to prevent ID conflicts
- Primary 6 languages shown as tabs, remaining 13 in dropdown
- `code-tabs.js` adds interactivity without breaking core functionality

**CSS Styling:**
- Defined in `_sass/custom.scss` under `.code-tabs` class
- Dark mode variants in `_sass/dark-mode.scss`
- Responsive breakpoints for mobile devices
- Syntax highlighting via Rouge with custom dark theme

### Dark Mode System

**Architecture:**
1. **Detection**: Checks localStorage → CSS class → system preference
2. **Anti-flash**: Script runs in `<head>` before DOM render
3. **Toggle**: Floating button (bottom-right) with sun/moon icons
4. **Persistence**: Saves user preference to localStorage
5. **Styling**: CSS variables + theme-specific overrides

**Files:**
- `assets/js/dark-mode.js`: Toggle logic and initialization (176 lines)
- `_sass/dark-mode.scss`: Dark theme styles (346 lines)
- `_includes/dark-mode-toggle.html`: Toggle button HTML
- `_includes/custom-head.html`: Early script loading

**Features:**
- Three modes: light, dark, system
- Smooth transitions
- Custom syntax highlighting for dark mode
- Responsive button sizing
- Accessibility support

### Table of Contents System

**Features:**
- Auto-generated from H2 and H3 headings
- Scroll-spy using IntersectionObserver API
- Sticky positioning with smart collapse
- Auto-collapses when scrolling down (sticky state)
- Click to expand/collapse when sticky
- Only shows on post pages

**Implementation:**
- `_includes/toc.html`: Main component (205 lines)
- Vanilla JavaScript with IIFE pattern
- No dependencies
- Mobile-responsive with auto-collapse
- Smooth scroll animation

### Multi-Model Solution System

**Workflow:**
1. `generate_post_by_date.py` or `regenerate_solution_multi.py` is called
2. Script fetches problem and generates solutions from multiple models
3. `generate_post.py` creates collapsible `<details>` sections
4. Each section contains approach, code tabs, and complexity
5. First solution is `open` by default, others are collapsed
6. Model-specific emojis identify each solution (✨ Gemini, ⚡ Llama)

**Benefits:**
- Compare different AI approaches
- Learn from multiple perspectives
- Flexibility to use free-tier APIs from multiple providers

### Jekyll Configuration

**Theme**: Minima 2.5 (heavily customized)
**Markdown**: Kramdown with Rouge syntax highlighting
**Timezone**: Asia/Seoul (KST, UTC+9)
**Permalink**: `/:categories/:year/:month/:day/:title/`

**Navigation**:
- Archive (chronological by date)
- Difficulties (Easy, Medium, Hard)
- Tags (algorithmic topics)

**Custom Overrides**:
- `_layouts/home.html`: Hero section, statistics, recent posts grid
- `_layouts/post.html`: TOC, breadcrumbs, related posts, navigation
- `_sass/custom.scss`: 1602 lines of custom styling
- `_sass/dark-mode.scss`: 346 lines of dark theme

**Plugins**:
- `jekyll-feed`: RSS feed generation
- `jekyll-seo-tag`: SEO meta tags

## Important Patterns

### Date Handling
- Posts use `YYYY-MM-DD` format (e.g., `2025-11-18`)
- Filenames: `_posts/YYYY-MM-DD-title-slug.md`
- Frontmatter date: `YYYY-MM-DD 09:00:00 +0900` (KST)
- LeetCode API uses UTC, scripts convert to KST

### JSON Data Flow

**Single Model Workflow:**
```
fetch_leetcode.py → question_data.json
  → solve_with_ai.py → question_with_solution.json
  → generate_post.py → _posts/YYYY-MM-DD-slug.md
```

**Multi-Model Workflow:**
```
generate_post_by_date.py
  → fetches question
  → calls solve_with_ai.py for each model
  → aggregates solutions
  → calls generate_post.py with multiple solutions
  → _posts/YYYY-MM-DD-slug.md
```

### Code Tab ID Naming
- Use suffix parameter to create unique IDs: `code-tabs-{suffix}`
- Default suffix is `"default"`
- Multi-solution posts use model names as suffix: `"gemini"`, `"groq"`
- Prevents radio button conflicts when multiple tab sets exist

### ⚠️ CRITICAL: Jekyll Liquid Escaping for Code Blocks

**MUST ALWAYS wrap code with `{% raw %}` tags to prevent Liquid parsing errors!**

**Problem**: Jekyll's Liquid template engine parses `{{` and `}}` as variables BEFORE syntax highlighting. This causes build failures when code contains these characters (common in Go, Python, Rust, etc.).

**Example Conflicts**:
- **Go**: `[][]int{{1, 2}, {3, 4}}` → Liquid tries to parse `{{1, 2}`
- **Python**: `f"{{value}}"` → Liquid error
- **Rust**: `macro_rules! { ... {{ ... }} }` → Liquid error

**Required Pattern in `generate_post.py`** (lines 143-147):
```python
tabs_html.append('{%% highlight %s %%}\n' % fence)
tabs_html.append('{% raw %}\n')        # ← CRITICAL: Must not be removed!
tabs_html.append(code + '\n')
tabs_html.append('{% endraw %}\n')     # ← CRITICAL: Must not be removed!
tabs_html.append('{% endhighlight %}\n\n')
```

**Why This Matters**:
- Without `{% raw %}`, posts with Go/Python/Rust code will fail Jekyll build
- AI-generated code naturally contains `{{` patterns
- Removing these tags breaks the site build
- Affects ~30% of LeetCode problems (those using affected languages)

**DO NOT REMOVE** the `{% raw %}` and `{% endraw %}` tags when modifying code generation!

### ⚠️ CRITICAL: Code Indentation Normalization

**MUST always dedent AI-generated code to remove extra indentation!**

**Problem**: Some AI models (especially Llama) generate code with extra leading indentation (e.g., 7 extra spaces on every line). This makes the code look unprofessional and inconsistent across different AI solutions.

**Example Issue:**
```cpp
// Gemini (correct)
class Solution {
public:
    int solve() {

// Llama (wrong - extra 7 spaces)
class Solution {
       public:
           int solve() {
```

**Required Pattern in `solve_with_ai.py`** (lines 175-178):
```python
# Remove leading/trailing whitespace
cleaned = cleaned.strip()

# Remove common leading indentation from all lines (fixes Llama extra indentation)
cleaned = textwrap.dedent(cleaned)  # ← CRITICAL: Must not be removed!

return cleaned
```

**Why This Matters**:
- Ensures consistent code formatting across all AI models
- Removes extra indentation from Llama/Groq responses
- Preserves relative indentation within code (nested blocks)
- Works for all 19 programming languages
- Uses Python's `textwrap.dedent()` to find and remove common leading whitespace

**DO NOT REMOVE** the `textwrap.dedent()` call when modifying code cleaning!

### AI Solution Format

**Required Fields:**
```json
{
  "approach": "3-5 paragraph explanation...",
  "code": {
    "python": "...",
    "java": "...",
    "cpp": "...",
    "javascript": "...",
    "typescript": "...",
    "go": "...",
    "python3": "...",
    "c": "...",
    "csharp": "...",
    "php": "...",
    "swift": "...",
    "kotlin": "...",
    "dart": "...",
    "ruby": "...",
    "scala": "...",
    "rust": "...",
    "racket": "...",
    "erlang": "...",
    "elixir": "..."
  },
  "time_complexity": "O(...) explanation",
  "space_complexity": "O(...) explanation"
}
```

**Formatting Rules:**
- Approach: 3-5 paragraphs minimum
- Code: Properly formatted, no comments unless necessary
- Complexity: Big O notation with brief explanation

### Error Handling
- Scripts use `try/except` with stderr logging
- AI generation has graceful fallback (posts without solutions)
- Workflows continue on AI failure (`|| true` in workflow step)
- JSON validation with helpful error messages
- Git conflicts avoided by checking for existing posts

### HTML/Markdown Conversion
- `fetch_leetcode.py` uses BeautifulSoup and html2text
- Special handling for:
  - Tables → code blocks (markdown tables break Jekyll)
  - `<pre>` tags → triple backtick code blocks
  - Images → `![alt](url)` format
  - Nested HTML → recursive cleaning

### CSS Architecture
- **CSS Variables**: Defined in `:root` for easy theming
- **Dark Mode Override**: `.dark-mode` class overrides variables
- **Component-Based**: Each component (tabs, cards, hero) is self-contained
- **Mobile-First**: Base styles for mobile, media queries for desktop
- **Accessibility**: Focus-visible states, reduced-motion support

### JavaScript Patterns
- **IIFE**: All scripts use Immediately Invoked Function Expressions
- **No Dependencies**: Vanilla JavaScript only
- **Progressive Enhancement**: Core functionality works without JS
- **Event Delegation**: Efficient event handling
- **LocalStorage**: User preferences persist across sessions

## Development Workflow

This project uses Git Flow branching strategy:

### Branch Structure
- **`master`** (protected): Production, deployed to GitHub Pages
- **`develop`** (default): Main development, receives daily automated posts
- **`develop-feature-{name}-{id}`**: Individual feature branches

### Workflow
1. Create feature branch from `develop`
2. Make changes and commit
3. Push and create PR to `develop`
4. After review, merge to `develop`
5. Periodically merge `develop` → `master` for releases

See **BRANCHING_STRATEGY.md** for details.

### Testing Changes

**Before Pushing:**
1. Test Python scripts locally with sample JSON
2. Validate JSON output format
3. Test Jekyll build: `bundle exec jekyll serve`
4. Check responsive design (mobile, tablet, desktop)
5. Test dark mode toggle
6. Verify code tabs work with JS disabled
7. Validate YAML frontmatter
8. Check accessibility (keyboard navigation, screen readers)

**For CSS Changes:**
- Test in both light and dark modes
- Check all breakpoints (mobile, tablet, desktop)
- Verify reduced-motion preference is respected
- Test in multiple browsers

**For JavaScript Changes:**
- Test with browser DevTools console open
- Verify localStorage persistence
- Test error handling (network failures, missing data)
- Check performance (no jank during interactions)

**For Script Changes:**
- Run with sample data first
- Check error handling (missing API keys, network errors)
- Validate output format matches expected schema
- Test edge cases (missing fields, malformed HTML)

## GitHub Actions Workflows

### leetcode-daily.yml (Daily Automation)
**Schedule**: 00:00 UTC daily (09:00 KST)
**Triggers**: Schedule + manual dispatch
**Steps**:
1. Checkout repository
2. Set up Python and install dependencies
3. Fetch daily question from LeetCode
4. Generate AI solution (model selected via `AI_MODEL` input)
5. Create Jekyll post
6. Commit and push to `master` if new post created

**Environment Variables**:
- `AI_MODEL`: `gemini` or `groq` (default: `gemini`)
- `GEMINI_API_KEY`: Secret for Gemini API
- `GROQ_API_KEY`: Secret for Groq API

### regenerate-solution.yml (Manual Regeneration)
**Triggers**: Manual dispatch only
**Inputs**:
- `date`: Post date in YYYY-MM-DD format
- `model`: Choose from `gemini`, `groq`, or `Both (gemini + llama)`

**Behavior**:
- If single model: Uses `regenerate_solution.py`
- If "Both": Uses `regenerate_solution_multi.py` for collapsible sections
- Updates existing post with new solutions
- Commits to current branch

### generate-post-by-date.yml (Generate by Date)
**Triggers**: Manual dispatch only
**Inputs**:
- `date`: Date in YYYY-MM-DD format
- `models`: Space-separated model names (e.g., `gemini groq`)

**Behavior**:
- Uses `generate_post_by_date.py`
- Generates post with multiple AI solutions
- Useful for backfilling missing dates
- Commits to current branch

## Key Constraints

### LeetCode API
- Only provides "today's" daily question via GraphQL
- No official API for historical daily questions
- Regeneration works if problem is still accessible by slug
- Rate limiting: Be respectful, use delays in batch operations

### AI API Limits
- **Gemini**: Free tier has rate limits (check Google AI Studio)
- **Groq**: Free tier has rate limits (check Groq Console)
- Scripts handle rate limit errors gracefully
- Use delays between batch requests (see `batch_regenerate.py`)

### GitHub Pages
- Jekyll 4.3.0 supported
- Some plugins not available (GitHub Pages whitelist)
- Build time increases with more posts
- Static site only (no server-side logic)

### Browser Compatibility
- Dark mode: Modern browsers with CSS variables support
- Code tabs: Works without JS (progressive enhancement)
- IntersectionObserver: No IE11 support (consider polyfill if needed)
- LocalStorage: Check availability before use

## Dependencies

### Python (scripts/requirements.txt)
```
requests==2.31.0              # HTTP client for LeetCode and AI APIs
python-dateutil==2.8.2        # Date parsing and manipulation
google-generativeai==0.8.3    # Gemini API client
beautifulsoup4==4.12.3        # HTML parsing
html2text==2024.2.26          # HTML to Markdown conversion
```

**Installation**: `pip install -r scripts/requirements.txt`

### Ruby (Gemfile)
```ruby
jekyll (~> 4.3.0)     # Static site generator
minima (~> 2.5)       # Base theme (heavily customized)
jekyll-feed (~> 0.12) # RSS feed generation
jekyll-seo-tag (~> 2.8) # SEO meta tags
```

**Installation**: `bundle install`

### JavaScript
- **No external dependencies**
- Vanilla JavaScript only
- Modern browser APIs: IntersectionObserver, localStorage
- Progressive enhancement approach

## Troubleshooting

### Post Generation Issues
- **Missing AI solution**: Check API key environment variable
- **Duplicate post error**: Script skips if file exists, check `_posts/` directory
- **JSON parsing error**: Validate JSON with online validator, check AI response format
- **HTML conversion issues**: Check `fetch_leetcode.py` for BeautifulSoup errors

### Jekyll Build Issues
- **YAML frontmatter error**: Validate YAML syntax, check for special characters
- **Markdown rendering**: Tables should be converted to code blocks
- **Syntax highlighting**: Ensure language is supported by Rouge
- **Missing includes**: Check `_includes/` directory for required files

### Dark Mode Issues
- **Flash on load**: Ensure `dark-mode.js` is loaded in `<head>` before body
- **Theme not persisting**: Check localStorage availability in browser
- **Styles not applying**: Check CSS specificity, verify dark-mode class is added

### Code Tab Issues
- **Tabs not switching**: Check radio input names match (use unique suffix)
- **Dropdown not working**: Verify `code-tabs.js` is loaded
- **Language preference not saved**: Check localStorage errors in console
- **Multiple tab sets conflicting**: Ensure each set has unique suffix

### Git Workflow Issues
- **Merge conflicts**: Check if daily automation modified same file
- **CI/CD failure**: Check GitHub Actions logs, verify secrets are set
- **Push rejected**: Ensure you're on correct branch, check branch protection rules

## Performance Optimization

### Jekyll Build Time
- Use `--incremental` flag for faster rebuilds during development
- Limit post count in development: `limit: 10` in `_config.yml` (dev only)
- Pre-generate posts and commit (done by CI)

### Page Load Time
- Minify CSS/JS in production (add build step if needed)
- Optimize images (use appropriate formats and sizes)
- Lazy load images below the fold
- Use CDN for static assets if traffic increases

### JavaScript Performance
- IntersectionObserver is efficient (use native API)
- LocalStorage reads are synchronous but fast
- Debounce scroll events if adding custom handlers
- Use event delegation for dynamic elements

## Security Considerations

### API Keys
- **Never commit**: Use environment variables only
- **GitHub Secrets**: Store in repository settings
- **Local Development**: Use `.env` file (add to `.gitignore`)
- **Rotate Regularly**: Change keys periodically

### User Input
- Posts are generated from LeetCode API (trusted source)
- No user-submitted content in production
- Markdown conversion escapes HTML by default

### Third-Party Scripts
- AdSense: Only include if needed, verify source
- Analytics: Consider privacy-friendly alternatives
- No external CDNs for critical functionality (self-host JS/CSS)

## Additional Resources

### Documentation
- **Jekyll**: https://jekyllrb.com/docs/
- **Minima Theme**: https://github.com/jekyll/minima
- **LeetCode API**: GraphQL endpoint at https://leetcode.com/graphql
- **Gemini API**: https://ai.google.dev/docs
- **Groq API**: https://console.groq.com/docs

### Tools
- **Markdown**: https://www.markdownguide.org/
- **YAML Validator**: https://www.yamllint.com/
- **JSON Validator**: https://jsonlint.com/
- **Rouge Supported Languages**: https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers

---

Last Updated: 2025-11-18
Version: 2.0
Maintained by: scavienger
