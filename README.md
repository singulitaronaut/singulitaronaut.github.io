# Markdown Blog Generator

A static blog generator that converts markdown files with YAML frontmatter into a beautiful HTML blog, automatically deployed via GitHub Actions.

## Features

- 📝 Write posts in Markdown with YAML frontmatter
- 🎨 Beautiful, responsive HTML templates
- 🚀 Automatic deployment to GitHub Pages
- 📱 Mobile-friendly design
- 🔍 SEO optimized with meta tags
- 📊 Social media preview cards
- 📅 Automatic post sorting by date

## Getting Started

### 1. Repository Setup

1. Fork or clone this repository
2. Enable GitHub Pages in your repository settings:
   - Go to Settings → Pages
   - Set Source to "GitHub Actions"

### 2. Writing Posts

Create markdown files in the `posts/` directory with the following frontmatter:

```markdown
---
title: Your Post Title
description: A brief description of your post
date: 2024-01-15
author: Your Name
tags: [tag1, tag2]
---

# Your Post Content

Write your markdown content here...
```

### 3. Customization

- Edit `templates/base.html` to customize the overall layout
- Edit `templates/post.html` to customize individual post pages
- Edit `templates/index.html` to customize the homepage
- Modify `static/style.css` for styling changes

### 4. Deployment

Simply push your changes to the main branch. GitHub Actions will automatically:
1. Convert your markdown files to HTML
2. Generate the homepage with post previews
3. Deploy everything to GitHub Pages

Your blog will be available at `https://yourusername.github.io/your-repo-name/`

## File Structure

```
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions workflow
├── posts/                  # Your markdown blog posts
├── templates/              # Jinja2 HTML templates
├── static/                 # CSS, JS, images
├── scripts/               # Build scripts
├── docs/                  # Generated HTML (GitHub Pages source)
└── pyproject.toml         # Project dependencies
```

## Frontmatter Fields

### Required Fields
- `title`: Post title
- `description`: Brief description for SEO and previews
- `date`: Publication date (YYYY-MM-DD format)

### Optional Fields
- `author`: Author name
- `tags`: List of tags
- `image`: Featured image URL
- `draft`: Set to `true` to exclude from build
- Any custom fields you want to include

## Local Development

To test locally, you'll need [uv](https://docs.astral.sh/uv/) installed:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Build the blog
uv run scripts/build.py

# Serve the docs/ directory with any static file server
# For example, with Python:
python -m http.server 8000 --directory docs
```

Then open http://localhost:8000 in your browser to view your blog.

## Dependencies

This project uses `uv` for dependency management. Dependencies are defined in `pyproject.toml`:

- **markdown**: Convert markdown to HTML
- **Jinja2**: HTML templating engine
- **PyYAML**: Parse YAML frontmatter
- **python-frontmatter**: Extract frontmatter from markdown files
- **Pillow**: Image processing (for potential future features)

## Compatibility with Reprose

This blog generator is designed to work seamlessly with [Reprose](https://reprose.pp.ua/), an online markdown editor that integrates with GitHub. You can:

1. Write and edit posts directly in Reprose
2. Push changes to your repository
3. Watch as GitHub Actions automatically builds and deploys your blog

The frontmatter format is fully compatible with Reprose's standard fields (`title`, `description`, `date`) and supports any additional custom fields you want to add. 