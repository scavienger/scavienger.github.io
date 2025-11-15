# LeetCode Daily Challenge Blog

Automated blog that fetches and posts LeetCode Daily Challenge problems every day at 9:00 AM KST.

## Features

- **Automated Daily Posts**: GitHub Actions fetches the daily LeetCode problem and creates a new blog post automatically
- **AI-Generated Solutions**: Free AI providers (Gemini or Groq) generate solutions automatically
- **Multiple AI Providers**: Choose from Gemini (default) or Groq (Llama 3.3) - both with free tiers
- **Jekyll-powered**: Clean, fast static site hosted on GitHub Pages
- **Modern UI**: Beautiful, responsive design with dark mode support
- **Navigation**: Archive, difficulty, and topic-based browsing
- **AdSense Ready**: Pre-configured layout with AdSense placeholder slots

## Project Structure

```
scavienger.github.io/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Home page
├── _layouts/
│   └── post.html           # Post layout with AdSense placeholders
├── _posts/                 # Auto-generated blog posts
├── .github/
│   └── workflows/
│       └── leetcode-daily.yml  # GitHub Actions workflow
└── scripts/
    ├── requirements.txt        # Python dependencies
    ├── fetch_leetcode.py       # Fetches daily question from LeetCode
    ├── solve_with_ai.py        # Generates solutions using AI models
    └── generate_post.py        # Generates Jekyll markdown post
```

## How It Works

1. **Scheduled Trigger**: GitHub Actions runs daily at 9:00 AM KST
2. **Fetch Question**: `fetch_leetcode.py` queries LeetCode's GraphQL API
3. **AI Solutions**: `solve_with_ai.py` generates solutions using Claude, GPT-4, and Gemini
4. **Generate Post**: `generate_post.py` creates a markdown file with all solutions in `_posts/`
5. **Auto Deploy**: GitHub Pages automatically builds and deploys the updated site

## Setup Instructions

### 1. Enable GitHub Pages

1. Go to repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: Select your main branch and `/root` folder
4. Save

### 2. Enable GitHub Actions Permissions

1. Go to repository Settings → Actions → General
2. Workflow permissions: Select "Read and write permissions"
3. Save

### 3. Configure AI Provider (Optional but Recommended)

To enable AI-generated solutions, configure your preferred AI provider:

#### Choose Your AI Provider

Both providers offer free tiers!

| Provider | Model | Secret Name | Get API Key |
|----------|-------|-------------|-------------|
| **Gemini** (Default) ✨ | gemini-2.5-flash | `GEMINI_API_KEY` | [Get Key](https://aistudio.google.com/app/apikey) |
| **Groq** ⚡ | llama-3.3-70b-versatile | `GROQ_API_KEY` | [Get Key](https://console.groq.com/keys) |

#### Setup Instructions

1. **Add API Key to GitHub Secrets**
   - Go to repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Add `GEMINI_API_KEY` (for Gemini) or `GROQ_API_KEY` (for Groq)

2. **Change Provider (Optional)**
   - Default provider is **Gemini**
   - To use **Groq** instead, edit `.github/workflows/leetcode-daily.yml`:
   ```yaml
   env:
     AI_PROVIDER: groq  # Change from 'gemini' to 'groq'
   ```

**Notes:**
- Only API keys go in Secrets (sensitive data)
- Provider selection is in the workflow file (not sensitive)
- Both providers offer generous free tiers
- Without any API key, posts will only have problem descriptions without solutions

### 4. Test the Workflow

You can manually trigger the workflow to test:

1. Go to Actions tab
2. Select "LeetCode Daily Challenge" workflow
3. Click "Run workflow"

### 5. Configure AdSense (Optional)

#### Step 1: Add Site Verification Code

When you first add your site to AdSense, you'll receive a verification code like:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX"
     crossorigin="anonymous"></script>
```

1. Open `_includes/custom-head.html`
2. Replace the comment with your actual AdSense verification code
3. Commit and push the changes
4. Wait for AdSense approval (can take a few days to weeks)

#### Step 2: Add Ad Units (After Approval)

After your site is approved:

1. Create ad units in AdSense console
2. Copy the complete ad code snippet (includes `<ins>` tags)
3. Open `_layouts/post.html`
4. Replace the commented placeholders with your actual ad code
5. Commit and push the changes

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

# Fetch today's question
python scripts/fetch_leetcode.py > question_data.json

# Generate a post
python scripts/generate_post.py < question_data.json
```

## Customization

### Modify Posting Schedule

Edit `.github/workflows/leetcode-daily.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Change this cron expression
```

Current: 00:00 UTC = 09:00 KST

### Customize Theme

The site uses the Minima theme. You can:

- Override styles in `_sass/` directory
- Modify layouts in `_layouts/`
- Update `_config.yml` for site settings

## Troubleshooting

### Posts Not Appearing

1. Check GitHub Actions logs for errors
2. Ensure workflow has write permissions
3. Verify `_posts/` directory has new files

### Build Failures

1. Check Jekyll build logs in Actions
2. Validate markdown frontmatter format
3. Ensure all required gems are in Gemfile

## License

MIT License - Feel free to use this for your own LeetCode blog!

## Contributing

Issues and pull requests are welcome!
