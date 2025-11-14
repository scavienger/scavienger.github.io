# LeetCode Daily Challenge Blog

Automated blog that fetches and posts LeetCode Daily Challenge problems every day at 9:00 AM KST.

## Features

- **Automated Daily Posts**: GitHub Actions fetches the daily LeetCode problem and creates a new blog post automatically
- **Jekyll-powered**: Clean, fast static site hosted on GitHub Pages
- **AdSense Ready**: Pre-configured layout with AdSense placeholder slots
- **Problem Details**: Each post includes problem description, hints, code template, and solution structure

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
    └── generate_post.py        # Generates Jekyll markdown post
```

## How It Works

1. **Scheduled Trigger**: GitHub Actions runs daily at 9:00 AM KST
2. **Fetch Question**: `fetch_leetcode.py` queries LeetCode's GraphQL API
3. **Generate Post**: `generate_post.py` creates a markdown file in `_posts/`
4. **Auto Deploy**: GitHub Pages automatically builds and deploys the updated site

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

### 3. Test the Workflow

You can manually trigger the workflow to test:

1. Go to Actions tab
2. Select "LeetCode Daily Challenge" workflow
3. Click "Run workflow"

### 4. Configure AdSense (Optional)

After your site is approved for AdSense:

1. Open `_layouts/post.html`
2. Uncomment the AdSense code blocks
3. Replace `ca-pub-XXXXXXXXXX` with your publisher ID
4. Replace `YYYYYYYYYY` with your ad slot IDs
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
