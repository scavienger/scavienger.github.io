# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an automated LeetCode Daily Challenge blog powered by Jekyll and GitHub Pages. The system fetches daily LeetCode problems at 00:00 UTC (midnight UTC) via GitHub Actions, generates AI solutions in 19 programming languages using multiple AI models, and publishes them as interactive blog posts with modern features like dark mode, table of contents, code copy buttons, and multi-language code tabs.

## Key Features

### User Interface
- **Dark Mode**: System preference detection with manual toggle, localStorage persistence, and anti-flash loading
- **Table of Contents**: Auto-generated from headings with scroll-spy, collapsible on mobile, smart sticky behavior
- **Code Tabs**: Pure CSS tabs for 19 programming languages with JavaScript enhancements for language preference persistence
- **Code Copy**: One-click copy button for all code blocks with visual feedback
- **Multiple AI Solutions**: Collapsible sections showing solutions from different AI models
- **Modern Design**: Hero section, statistics dashboard, card-based layout, breadcrumb navigation
- **Related Posts**: Automatic suggestions based on difficulty level
- **Responsive**: Mobile-first design with accessibility features

### Programming Languages

**All 19 Languages** (shown in tabs or dropdown):
1. C++
2. Java
3. Python
4. Python3
5. C
6. C#
7. JavaScript
8. TypeScript
9. PHP
10. Swift
11. Kotlin
12. Dart
13. Go
14. Ruby
15. Scala
16. Rust
17. Racket
18. Erlang
19. Elixir

### AI Models
- **Gemini 2.5 Flash** (Google, emoji: ✨): Fast, efficient, good at code generation
- **Llama 3.3 70B** (Groq, emoji: ⚡): Powerful open-source model, detailed explanations
- **Qwen 2.5 32B** (Groq, emoji: 🚀): Alternative Groq model
- **Groq Compound** (Groq, emoji: 🧬): Compound reasoning model

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

The project now uses a **unified generator script** (`generate_posts.py`) that handles fetching, solving, and post generation in one step.

```bash
# Generate post for today with default model (gemini-2.5-flash)
export GEMINI_API_KEY="your-key"
python scripts/generate_posts.py 2025-11-23

# Generate with specific model
python scripts/generate_posts.py 2025-11-23 llama-3.3-70b-versatile

# Generate with multiple AI models (creates collapsible sections)
export GEMINI_API_KEY="your-key"
export GROQ_API_KEY="your-key"
python scripts/generate_posts.py 2025-11-23 gemini-2.5-flash llama-3.3-70b-versatile

# Generate for date range
python scripts/generate_posts.py 2025-11-01 2025-11-10 gemini-2.5-flash
```

### Regenerate Solutions

To update existing posts with new AI solutions:

```bash
# Regenerate specific model for existing post (use defaults, only regen Llama)
export GROQ_API_KEY="your-key"
python scripts/generate_posts.py 2025-11-14 --update-models llama-3.3-70b-versatile

# Regenerate multiple models
export GEMINI_API_KEY="your-key"
export GROQ_API_KEY="your-key"
python scripts/generate_posts.py 2025-11-14 gemini-2.5-flash llama-3.3-70b-versatile --update-models gemini-2.5-flash,llama-3.3-70b-versatile

Note: `--update-models` filters within the currently active model set. If you omit positional models, the defaults (`gemini-2.5-flash`, `llama-3.3-70b-versatile`) are used. To regen a non-default model (e.g., `qwen-2.5-32b`), add it positionally alongside `--update-models qwen-2.5-32b`.
```

You can also trigger regeneration via GitHub Actions:
- **"Regenerate AI Solution for Post"**: Select date and model(s) to regenerate
- **"Generate Post by Date"**: Generate post for specific date with multiple models

### JavaScript Development

The project uses vanilla JavaScript (no build process) for:
- **Dark mode**: `assets/js/dark-mode.js`
- **Code tabs**: `assets/js/code-tabs.js`
- **Code copy**: `assets/js/code-copy.js`

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
├── _posts/                      # Generated blog posts (nested structure)
│   └── _daily/                 # Daily challenges
│       └── YYYY/MM/DD/         # Year/Month/Day folders
│           ├── slug.md         # Post file (no date prefix)
│           ├── python.txt      # Python code snippet
│           ├── java.txt        # Java code snippet
│           └── ...             # Other language snippets
├── _sass/                       # SCSS stylesheets
│   ├── custom.scss             # Main styles
│   └── dark-mode.scss          # Dark mode theme overrides
├── assets/js/                   # JavaScript files
│   ├── dark-mode.js            # Dark mode toggle logic
│   ├── code-tabs.js            # Code tab interactions
│   └── code-copy.js            # Code copy functionality
├── scripts/                     # Python automation
│   ├── generate_posts.py       # ⭐ Unified generator (fetch + solve + post)
│   ├── solve_with_ai.py        # Generate solution with AI model
│   ├── generate_post.py        # Create Jekyll markdown post
│   └── requirements.txt        # Python dependencies
├── data/                        # Cache files
│   └── daily_challenges.json   # Cached daily challenge mappings
├── _config.yml                  # Jekyll configuration
├── Gemfile                      # Ruby dependencies
└── CLAUDE.md                    # This file
```

### Automation Pipeline

The daily automation workflow (`.github/workflows/leetcode-daily.yml`) runs at 00:00 UTC (midnight UTC):

1. **generate_posts.py**: Unified script that handles everything
   - Fetches daily challenges from LeetCode GraphQL API (dailyCodingChallengeV2)
   - Caches challenge mappings (date → link, titleSlug) in `data/daily_challenges.json`
   - Fetches problem details by titleSlug via GraphQL (question query)
   - Saves code snippets for all 19 languages to `_posts/_daily/YYYY/MM/DD/{lang}.txt`
   - Calls `solve_with_ai.py` to generate AI solutions for each specified model
   - Calls `generate_post.py` to create Jekyll markdown post
   - Outputs to `_posts/_daily/YYYY/MM/DD/{slug}.md` (nested structure, no date prefix)

2. **solve_with_ai.py**: Generates AI solution
   - Supports 4 models: `gemini-2.5-flash`, `llama-3.3-70b-versatile`, `qwen-2.5-32b`, `groq/compound`
   - Model selected via `AI_MODEL` environment variable
   - Prompts AI with strict JSON format requirements:
     - `approach`: 3 paragraph explanation (detailed)
     - `solutions`: Code in all 19 languages
     - `time_complexity`: Big O with explanation
     - `space_complexity`: Big O with explanation
   - **Indentation Normalization**: Automatically detects and removes excess indentation from AI-generated code using `textwrap.dedent()` and template comparison
   - Validates JSON response and extracts solution
   - Gracefully falls back if API key missing (posts without solutions)
   - Returns solution with `elapsed_time` metadata

3. **generate_post.py**: Creates Jekyll markdown post
   - Generates YAML frontmatter (title, date, tags, difficulty, leetcode_url)
   - Builds problem description with examples and constraints
   - Creates collapsible `<details>` sections for multiple AI solutions (with `markdown="1"` attribute)
   - Generates Pure CSS code tabs with unique IDs for each solution
   - Wraps all code blocks with `{% raw %}` and `{% endraw %}` to prevent Liquid parsing errors
   - Outputs to nested directory: `_posts/_daily/YYYY/MM/DD/{slug}.md`

### Post Structure

Generated posts follow this structure:

```markdown
---
layout: post
title: "Problem Title"
date: YYYY-MM-DD 09:00:00 +0900
categories: [LeetCode, Difficulty]
tags: [topic1, topic2, ...]
difficulty: Easy/Medium/Hard
leetcode_url: https://leetcode.com/problems/...
---

## Problem #ID: Title
**Difficulty:** Easy/Medium/Hard
**Topics:** topic1, topic2, ...

## Problem Description
[Problem content in markdown]

### Illustrations
[Images if any]

## Hints
[LeetCode hints if available]

## 🤖 AI-Generated Solutions

<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(YYYY-MM-DD HH:MM:SS)</small>
</summary>
<div class="ai-solution-content">

### Approach
[3 paragraph explanation]

### Code
[Pure CSS code tabs for 19 languages]

### Complexity Analysis
- **Time Complexity**: O(...)
- **Space Complexity**: O(...)

</div>
</details>

<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(YYYY-MM-DD HH:MM:SS)</small>
</summary>
[Similar structure]
</details>
```

### Code Tab System

The code tabs use Pure CSS with JavaScript enhancement:
- **Pure CSS** for basic tab switching (works without JavaScript)
- **JavaScript enhancement** (`code-tabs.js`) for:
  - User language preference persistence (localStorage)
  - Automatic language selection on page load
- Radio inputs control tab switching (`name="code-lang{suffix}"`)
- Each AI solution gets unique suffix to prevent ID conflicts
- All 19 languages rendered in tabs

**Implementation Details:**
- Defined in `_sass/custom.scss` under `.code-tabs` class
- Dark mode variants in `_sass/dark-mode.scss`
- Syntax highlighting via Rouge with custom dark theme
- Each language gets unique radio input ID: `lang-{language}{suffix}`

### Code Copy System

**Features:**
- Copy button on all syntax-highlighted code blocks
- Visual feedback (✅ Copied / Failed)
- Clipboard API with fallback for older browsers
- MutationObserver for dynamically loaded content

**Implementation:**
- `assets/js/code-copy.js`: Copy functionality (155 lines)
- Targets `.highlight pre` elements (excludes plain `<pre>` in problem descriptions)
- Wraps code blocks with `.code-block-wrapper` for button positioning

### Dark Mode System

**Architecture:**
1. **Detection**: Checks localStorage → system preference
2. **Anti-flash**: Script runs in `<head>` before DOM render
3. **Toggle**: Floating button (bottom-right) with sun/moon icons
4. **Persistence**: Saves user preference to localStorage
5. **Styling**: CSS variables + theme-specific overrides

**Files:**
- `assets/js/dark-mode.js`: Toggle logic and initialization (55 lines)
- `_sass/dark-mode.scss`: Dark theme styles
- `_includes/dark-mode-toggle.html`: Toggle button HTML
- `_includes/custom-head.html`: Early script loading

**Features:**
- Two modes: light, dark (respects system preference if no saved preference)
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

### Caching System

**Purpose:** Avoid repeated API calls to fetch daily challenge mappings

**Implementation:**
- `data/daily_challenges.json`: Maps dates to problem metadata
  ```json
  {
    "2025-11-23": {
      "link": "/problems/problem-slug/",
      "titleSlug": "problem-slug"
    }
  }
  ```
- Cache updated automatically when generating posts for missing dates
- Uses GraphQL query `dailyCodingChallengeV2(year, month)` to fetch month data at once

**Benefits:**
- Fast post regeneration (no need to scrape problemset page)
- Reduced API calls
- Reliable date-to-problem mapping

### Code Snippet System

**Purpose:** Store LeetCode's official code templates for each language

**Storage Location:**
- Nested: `_posts/_daily/YYYY/MM/DD/{lang_slug}.txt`
- Legacy: `_posts/_snippets/{problem_slug}/{lang_slug}.txt`

**Usage:**
- Used by `solve_with_ai.py` to detect excess indentation in AI-generated code
- Compares AI code with official template to identify indentation bugs
- Helps normalize code formatting across different AI models

**Example:**
```
_posts/_daily/2025/11/23/
├── two-sum.md              # Post file
├── python.txt              # Python template
├── java.txt                # Java template
├── cpp.txt                 # C++ template
└── ...                     # Other languages
```

### Indentation Normalization System

**Problem:** Some AI models (especially Llama) generate code with extra leading indentation (e.g., 7 extra spaces on every line).

**Solution:** `solve_with_ai.py` implements multi-level indentation correction:

1. **Basic Dedent:** `textwrap.dedent()` removes common leading whitespace
2. **Template Comparison:** Compares AI code with LeetCode's official template
   - Finds matching lines between AI code and template
   - Calculates indentation difference
   - Detects excess indentation (≥7 spaces)
3. **Dynamic Analysis:** Falls back to statistical analysis if template unavailable
   - Analyzes first 10 non-empty lines
   - Detects fixed excess indentation
   - Preserves natural indentation unit (2 or 4 spaces)

**Key Functions:**
- `_clean_code()`: Main cleaning function with multi-stage correction
- `_detect_excess_from_template()`: Template-based correction
- `_detect_indent_unit()`: Determines indentation style from template
- `_find_matching_line()`: Matches AI code lines with template

**Why This Matters:**
- Ensures consistent code formatting across all AI models
- Removes Llama/Groq's common 7-space indentation bug
- Preserves relative indentation within code (nested blocks)
- Works for all 19 programming languages

### Multi-Model Solution System

**Workflow:**
1. `generate_posts.py` is called with multiple model names
2. Script fetches problem and generates solutions from each model
3. `generate_post.py` creates collapsible `<details>` sections
4. Each section contains approach, code tabs, and complexity
5. First solution is `open` by default, others are collapsed
6. Model-specific emojis identify each solution (✨ Gemini, ⚡ Llama, 🚀 Qwen, 🧬 Compound)

**Benefits:**
- Compare different AI approaches
- Learn from multiple perspectives
- Flexibility to use free-tier APIs from multiple providers

### Jekyll Configuration

**Theme**: Minima 2.5 (heavily customized)
**Markdown**: Kramdown with Rouge syntax highlighting
**Timezone**: Asia/Seoul (for post date display)
**Permalink**: `/:year/:month/:day/:title/`

**Collections:**
- `_daily`: Daily challenge posts (nested under `_posts/_daily/`)
- Output to `/:year/:month/:day/:title/` permalink

**Navigation**:
- Archive (chronological by date)
- Difficulties (Easy, Medium, Hard)
- Tags (algorithmic topics)

**Custom Overrides**:
- `_layouts/home.html`: Hero section, statistics, recent posts grid
- `_layouts/post.html`: TOC, breadcrumbs, related posts, navigation
- `_sass/custom.scss`: Custom styling
- `_sass/dark-mode.scss`: Dark theme

**Plugins**:
- `jekyll-feed`: RSS feed generation
- `jekyll-seo-tag`: SEO meta tags

**Exclusions:**
- `**/*.txt`: Exclude snippet files from being processed as pages

## Important Patterns

### Date Handling
- Posts use `YYYY-MM-DD` format (e.g., `2025-11-23`)
- Filenames: `_posts/_daily/YYYY/MM/DD/slug.md` (NO date prefix in filename)
- Frontmatter date: `YYYY-MM-DD 09:00:00 +0900` (displayed in Asia/Seoul timezone)
- LeetCode Daily Challenge resets at 00:00 UTC (midnight UTC)

### Unified Generator Workflow

**Single Model:**
```
generate_posts.py 2025-11-23 gemini-2.5-flash
  → Fetch from cache or GraphQL API
  → Fetch problem details (GraphQL)
  → Save code snippets
  → Call solve_with_ai.py (model=gemini-2.5-flash)
  → Call generate_post.py
  → _posts/_daily/2025/11/23/{slug}.md
```

**Multi-Model:**
```
generate_posts.py 2025-11-23 gemini-2.5-flash llama-3.3-70b-versatile
  → Fetch from cache or GraphQL API
  → Fetch problem details (GraphQL)
  → Save code snippets
  → Call solve_with_ai.py for each model
  → Aggregate solutions
  → Call generate_post.py with multiple solutions
  → _posts/_daily/2025/11/23/{slug}.md
```

**Regeneration with Update:**
```
generate_posts.py 2025-11-14 --update-models gemini-2.5-flash
  → Load existing post
  → Fetch problem details
  → Generate only specified model(s) (defaults list still used for validation)
  → Merge with existing solutions (replace same model)
  → Overwrite post
```

### Code Tab ID Naming
- Use suffix parameter to create unique IDs: `code-lang{suffix}`
- Default suffix is `""` (empty string)
- Multi-solution posts use model names as suffix: `"-gemini-2-5-flash"`, `"-llama-3-3-70b-versatile"`
- Prevents radio button conflicts when multiple tab sets exist

### ⚠️ CRITICAL: Jekyll Liquid Escaping for Code Blocks

**MUST ALWAYS wrap code with `{% raw %}` tags to prevent Liquid parsing errors!**

**Problem**: Jekyll's Liquid template engine parses `{{` and `}}` as variables BEFORE syntax highlighting. This causes build failures when code contains these characters (common in Go, Python, Rust, etc.).

**Example Conflicts**:
- **Go**: `[][]int{{1, 2}, {3, 4}}` → Liquid tries to parse `{{1, 2}`
- **Python**: `f"{{value}}"` → Liquid error
- **Rust**: `macro_rules! { ... {{ ... }} }` → Liquid error

**Required Pattern in `generate_post.py`** (lines 149-153):
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

**Required Pattern in `solve_with_ai.py`** (lines 279-282):
```python
# Remove leading/trailing whitespace
cleaned = cleaned.strip()

# Remove common leading indentation from all lines (fixes Llama extra indentation)
cleaned = textwrap.dedent(cleaned)  # ← CRITICAL: Must not be removed!
```

**Advanced Correction** (lines 284-351):
```python
# Try snippet-based correction if we have both problem_slug and lang_slug
if problem_slug and lang_slug:
    template = self._load_snippet(problem_slug, lang_slug, problem_date)
    if template:
        excess = self._detect_excess_from_template(cleaned, template)
        if excess and excess >= 7:
            # Remove detected excess indentation
            ...

# Fallback: Dynamic analysis for fixed excess indentation
# Analyzes first 10 lines, detects excess, preserves natural indent unit
...
```

**Why This Matters**:
- Ensures consistent code formatting across all AI models
- Removes extra indentation from Llama/Groq responses
- Preserves relative indentation within code (nested blocks)
- Works for all 19 programming languages
- Uses both template comparison and statistical analysis

**DO NOT REMOVE** the `textwrap.dedent()` call or indentation correction logic when modifying code cleaning!

### AI Solution Format

**Required Fields:**
```json
{
  "approach": "3 paragraph detailed explanation...",
  "time_complexity": "O(...) with explanation",
  "space_complexity": "O(...) with explanation",
  "solutions": {
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
  }
}
```

**Formatting Rules:**
- Approach: 3 paragraphs (detailed, educational)
- Code: Properly formatted with line breaks and indentation
- Complexity: Big O notation with brief explanation
- Model name and timestamp added by `solve_with_ai.py`

### Error Handling
- Scripts use `try/except` with stderr logging
- AI generation has graceful fallback (posts without solutions)
- Workflows continue on AI failure
- JSON validation with helpful error messages
- Cache system prevents duplicate API calls

### HTML/Markdown Conversion
- Problem content comes from GraphQL API in HTML format
- Minimal HTML cleaning in `generate_post.py`
- LeetCode API provides cleaner content than web scraping
- Images extracted and embedded in markdown

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
6. Verify code tabs work
7. Test code copy buttons
8. Validate YAML frontmatter
9. Check accessibility (keyboard navigation, screen readers)

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
- Test indentation correction with different AI models

## GitHub Actions Workflows

### leetcode-daily.yml (Daily Automation)
**Schedule**: 00:00 UTC daily (midnight UTC)
**Triggers**: Schedule + manual dispatch + push to develop (testing)
**Steps**:
1. Checkout repository (master branch)
2. Set up Python and install dependencies
3. Run `generate_posts.py` with specified model(s)
4. Commit and push to master if new post created

**Manual Trigger Inputs**:
- `ai_model`: Choose from `gemini-2.5-flash` or `llama-3.3-70b-versatile` (default: gemini)

**Environment Variables**:
- `GEMINI_API_KEY`: Secret for Gemini API
- `GROQ_API_KEY`: Secret for Groq API

### regenerate-solution.yml (Manual Regeneration)
**Triggers**: Manual dispatch only
**Inputs**:
- `date`: Post date in YYYY-MM-DD format
- `ai_models`: Choose from single model or "Both (gemini + llama)"

**Behavior**:
- Uses `generate_posts.py` with `--update-models` flag
- Updates existing post with new solutions
- Merges with existing solutions (replaces same model)
- Commits to master

### generate-post-by-date.yml (Generate by Date)
**Triggers**: Manual dispatch only
**Inputs**:
- `date`: Date in YYYY-MM-DD format
- `models`: Space-separated model names (default: both Gemini and Llama)

**Behavior**:
- Uses `generate_posts.py`
- Generates post with multiple AI solutions
- Useful for backfilling missing dates or regenerating old posts
- Commits to master

## Key Constraints

### LeetCode API
- GraphQL API provides reliable daily challenge data
- `dailyCodingChallengeV2` query fetches month data at once
- Problem details fetched by `titleSlug` via `question` query
- Rate limiting: Be respectful, use caching and delays in batch operations

### AI API Limits
- **Gemini**: Free tier has rate limits (check Google AI Studio)
- **Groq**: Free tier has rate limits (check Groq Console)
- Scripts handle rate limit errors gracefully
- Use delays between batch requests (5 seconds for Groq)
- Gemini supports up to 65536 output tokens

### GitHub Pages
- Jekyll 4.3.0 supported
- Some plugins not available (GitHub Pages whitelist)
- Build time increases with more posts
- Static site only (no server-side logic)
- Collections supported with `collections_dir` config

### Browser Compatibility
- Dark mode: Modern browsers with CSS variables support
- Code tabs: Pure CSS (works without JS)
- Code copy: Clipboard API with fallback for older browsers
- IntersectionObserver: No IE11 support (TOC gracefully degrades)
- LocalStorage: Check availability before use

## Dependencies

### Python (scripts/requirements.txt)
```
requests==2.31.0              # HTTP client for LeetCode and AI APIs
python-dateutil==2.8.2        # Date parsing and manipulation
google-generativeai==0.8.3    # Gemini API client
beautifulsoup4==4.12.3        # HTML parsing
html2text==2024.2.26          # HTML to Markdown conversion
PyYAML==6.0.2                 # YAML parsing for post frontmatter
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
- Modern browser APIs: IntersectionObserver, localStorage, Clipboard API
- Progressive enhancement approach

## Troubleshooting

### Post Generation Issues
- **Missing AI solution**: Check API key environment variable
- **Duplicate post error**: Script skips if file exists, regenerate with `--update-models`
- **JSON parsing error**: Validate JSON with online validator, check AI response format
- **Cache issues**: Delete `data/daily_challenges.json` to force refresh

### Jekyll Build Issues
- **YAML frontmatter error**: Validate YAML syntax, check for special characters
- **Markdown rendering**: Check for unescaped Liquid syntax (use `{% raw %}`)
- **Syntax highlighting**: Ensure language is supported by Rouge
- **Missing includes**: Check `_includes/` directory for required files
- **Collection not found**: Verify `collections_dir` and `_posts/_daily/` structure

### Dark Mode Issues
- **Flash on load**: Ensure `dark-mode.js` is loaded in `<head>` before body
- **Theme not persisting**: Check localStorage availability in browser
- **Styles not applying**: Check CSS specificity, verify dark-mode class is added

### Code Tab Issues
- **Tabs not switching**: Check radio input names match (use unique suffix)
- **Language preference not saved**: Check localStorage errors in console
- **Multiple tab sets conflicting**: Ensure each set has unique suffix

### Code Copy Issues
- **Button not appearing**: Check if code block has `.highlight` class
- **Copy fails**: Check Clipboard API availability, fallback should work
- **Wrong text copied**: Verify code extraction logic targets correct element

### Git Workflow Issues
- **Merge conflicts**: Check if daily automation modified same file
- **CI/CD failure**: Check GitHub Actions logs, verify secrets are set
- **Push rejected**: Ensure you're on correct branch, check branch protection rules

## Performance Optimization

### Jekyll Build Time
- Use `--incremental` flag for faster rebuilds during development
- Nested post structure helps Jekyll process files faster
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
- MutationObserver in code-copy.js is throttled

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
- **LeetCode GraphQL**: https://leetcode.com/graphql (introspection available)
- **Gemini API**: https://ai.google.dev/docs
- **Groq API**: https://console.groq.com/docs

### Tools
- **Markdown**: https://www.markdownguide.org/
- **YAML Validator**: https://www.yamllint.com/
- **JSON Validator**: https://jsonlint.com/
- **Rouge Supported Languages**: https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers

---

Last Updated: 2025-11-23
Version: 3.0
Maintained by: scavienger
