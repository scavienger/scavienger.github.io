# LeetCode Daily Challenge Blog

Automated blog that fetches and posts LeetCode Daily Challenge problems every day at 00:00 UTC (midnight UTC).

## Features

- **Automated Daily Posts**: GitHub Actions fetches the daily LeetCode problem and creates a new blog post automatically
- **AI-Generated Solutions**: Solutions in 19 programming languages with Pure CSS tabs
- **Gemini-only AI**: Gemini 3 Pro with Flash fallback on 429s
- **Manual Regeneration**: Update existing posts with new AI solutions via workflow or command line
- **Jekyll-powered**: Clean, fast static site hosted on GitHub Pages
- **Modern UI**: Beautiful, responsive design with dark mode support and code copy buttons
- **Navigation**: Archive, difficulty, and topic-based browsing
- **Smart Caching**: Efficient date-to-problem mapping for fast regeneration

## Quick Start

### 1. Enable GitHub Pages

1. Go to repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: Select `master` and `/root` folder
4. Save

### 2. Enable GitHub Actions Permissions

1. Go to repository Settings → Actions → General
2. Workflow permissions: Select "Read and write permissions"
3. Save

### 3. Configure AI Provider (Optional but Recommended)

To enable AI-generated solutions, add your API key:

#### Gemini (Only Provider)

| Provider | Model | Secret Name | Get API Key |
|----------|-------|-------------|-------------|
| **Gemini** ✨ | gemini-3-pro-preview (primary) / gemini-3-flash-preview (fallback) | `GEMINI_API_KEY` | [Get Key](https://aistudio.google.com/app/apikey) |

#### Setup Instructions

1. **Add API Key to GitHub Secrets**
   - Go to repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Add `GEMINI_API_KEY`

2. **Model Behavior**
   - Primary: **gemini-3-pro-preview**
   - If 429 occurs: auto-fallback to **gemini-3-flash-preview**
   - If flash also 429: sleep ~60s, retry pro

**Notes:**
- Only API keys go in Secrets (sensitive data)
- Without an API key, posts will only have problem descriptions without solutions

### 4. Test the Workflow

You can manually trigger the workflow to test:

1. Go to Actions tab
2. Select "LeetCode Daily Challenge" workflow
3. Click "Run workflow"
4. Choose AI model (default: Gemini)

## Project Structure

```
scavienger.github.io/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Home page
├── _layouts/
│   ├── home.html           # Homepage layout
│   └── post.html           # Post layout with TOC
├── _posts/                 # Auto-generated blog posts (nested by date)
│   └── _daily/             # Daily challenges
│       └── YYYY/MM/DD/     # Year/Month/Day folders
│           ├── slug.md     # Post file
│           └── *.txt       # Code snippets for each language
├── .github/
│   └── workflows/
│       ├── leetcode-daily.yml         # Daily automation workflow
│       ├── regenerate-solution.yml    # Manual regeneration workflow
│       └── generate-post-by-date.yml  # Generate by specific date
├── scripts/
│   ├── requirements.txt     # Python dependencies
│   ├── generate_posts.py    # Unified generator (fetch + solve + post)
│   ├── solve_with_ai.py     # AI solution generator
│   └── generate_post.py     # Jekyll post generator
├── data/                    # Cache files
│   └── daily_challenges.json   # Cached daily challenge mappings
└── assets/
    └── js/
        ├── dark-mode.js     # Dark mode toggle
        ├── code-tabs.js     # Code tab interactions
        └── code-copy.js     # Code copy functionality
```

## How It Works

### Daily Automation

1. **Scheduled Trigger**: GitHub Actions runs daily at 00:00 UTC (midnight UTC)
2. **Fetch Challenges**: Queries LeetCode GraphQL API for daily challenges
3. **Cache Mapping**: Stores date-to-problem mappings in `data/daily_challenges.json`
4. **Fetch Problem Details**: Gets problem content, examples, hints, and code templates
5. **Save Snippets**: Stores code templates for all 19 languages
6. **AI Solutions**: Generates solutions in 19 languages with approach and complexity analysis
7. **Generate Post**: Creates markdown file with Gemini solution and code tabs
8. **Auto Deploy**: GitHub Pages automatically builds and deploys the updated site

### Manual Regeneration

**Via GitHub Actions UI:**

1. Go to **Actions** → **Regenerate AI Solution for Post**
2. Click **Run workflow**
3. Enter the post date (YYYY-MM-DD format, e.g., `2025-11-23`)
4. Click **Run workflow**

**Via Command Line:**

```bash
# Set up environment
export GEMINI_API_KEY="your-key-here"

# Regenerate (Gemini only)
python scripts/generate_posts.py 2025-11-23
```

This is useful for:
- Regenerating solutions with improved prompts
- Adding solutions to posts that were created without AI keys

## AI Models

- **gemini-3-pro-preview** (primary)
- **gemini-3-flash-preview** (fallback on 429)

## Supported Programming Languages

All 19 languages supported by LeetCode:

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

## Local Development

### Prerequisites

- Ruby (>= 2.7)
- Bundler
- Python (>= 3.8)

### Running Locally

```bash
# Install Ruby dependencies
bundle install

# Serve the site locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Testing the Scripts

```bash
# Install Python dependencies
pip install -r scripts/requirements.txt

# Generate post for today
export GEMINI_API_KEY="your-key"
python scripts/generate_posts.py 2025-11-23

# Generate for date range
python scripts/generate_posts.py 2025-11-01 2025-11-10
```

## Customization

### Modify Posting Schedule

Edit `.github/workflows/leetcode-daily.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Change this cron expression
```

Current: 00:00 UTC (midnight UTC)

### Customize Theme

The site uses the Minima theme with heavy customizations:

- Override styles in `_sass/` directory
- Modify layouts in `_layouts/`
- Update `_config.yml` for site settings

## Troubleshooting

### Posts Not Appearing

1. Check GitHub Actions logs for errors
2. Ensure workflow has write permissions
3. Verify `_posts/_daily/` directory has new files

### Build Failures

1. Check Jekyll build logs in Actions
2. Validate markdown frontmatter format
3. Ensure all required gems are in Gemfile

### AI Solutions Missing

1. Verify API keys are added to GitHub Secrets
2. Check API key name: `GEMINI_API_KEY`
3. Check API rate limits (free tier has limits)

### Cache Issues

If you're having trouble with problem fetching:

```bash
# Delete cache to force refresh
rm data/daily_challenges.json
```

## Advanced Usage

### Batch Generation

Generate posts for multiple dates:

```bash
# Generate all posts for November 2025
python scripts/generate_posts.py 2025-11-01 2025-11-30
```

**Note:** This will make many API calls. Use delays between requests to avoid rate limiting.

### Caching System

The system caches daily challenge mappings in `data/daily_challenges.json`.

This cache allows fast regeneration without repeated API calls. The cache is automatically updated when generating posts for missing dates.

## Contributing

Issues and pull requests are welcome!

### Development Workflow

This project uses Git Flow branching strategy:

- **`master`**: Production, deployed to GitHub Pages
- **`develop`**: Main development branch
- **`develop-feature-{name}-{id}`**: Individual feature branches

See `BRANCHING_STRATEGY.md` for details.

## License

MIT License - Feel free to use this for your own LeetCode blog!

## Acknowledgments

- LeetCode for providing the daily challenge problems
- Google for Gemini API
- Gemini API for solution generation
- Jekyll and Minima theme

---

For detailed developer documentation, see **CLAUDE.md**.
