# Markdown Blog Generator

A static blog generator that converts markdown files with YAML frontmatter into a beautiful HTML blog, automatically deployed via GitHub Actions. Features a clean, monospace design inspired by [The Monospace Web](https://github.com/owickstrom/the-monospace-web/).

## Features

- 📝 Write posts in Markdown with YAML frontmatter
- 🎨 Beautiful, clean monospace design with JetBrains Mono font
- 🚀 Automatic deployment to GitHub Pages
- 📱 Mobile-friendly responsive design
- 🔍 SEO optimized with meta tags
- 📊 Social media preview cards
- 📅 Automatic post sorting by date
- 🎯 Debug grid for perfect typography alignment
- 🌙 Dark mode support (follows system preference)
- 🛠️ Rich utility classes for layout and components

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
- The design follows a strict grid system for perfect typography

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
│   ├── style.css          # Monospace web styling
│   ├── reset.css          # CSS reset
│   ├── index.js           # Grid alignment & debug tools
│   └── favicon.ico
├── scripts/build.py        # Blog generator script
├── docs/                  # Generated HTML (GitHub Pages source)
└── pyproject.toml         # Project dependencies
```

## Utility Classes & Components

The monospace design system includes powerful utility classes you can use in your markdown:

### Grid System
```html
<div class="grid">
  <p class="width-auto">Takes up most space</p>
  <p class="width-min">Minimal space</p>
</div>

<!-- Equal width columns (auto-detects 1-9 columns) -->
<div class="grid">
  <p>Column 1</p>
  <p>Column 2</p>
  <p>Column 3</p>
</div>
```

### Tree Structure
```html
<div class="tree">
  <ul>
    <li>Root Item
      <ul>
        <li>Child Item</li>
        <li>Another Child</li>
      </ul>
    </li>
  </ul>
</div>
```

### Interactive Elements
```html
<!-- Collapsible content -->
<details>
  <summary>Click to expand</summary>
  <p>Hidden content here</p>
</details>

<!-- Form elements in grid -->
<div class="grid">
  <label class="width-auto">
    Label text:
    <input type="text" placeholder="Input">
  </label>
  <button class="width-min">Submit</button>
</div>
```

### Width Utilities
- `.width-auto` - Takes available space (100%)
- `.width-min` - Minimal space (0%)

### Layout Components
- `.header` - Header styling with proper spacing
- `.debug-grid` - Visual grid overlay (auto-included)
- `.debug-toggle-label` - Right-aligned debug toggle

## Design Philosophy

This blog uses a monospace design system that:
- Aligns all content to a strict typographic grid
- Uses consistent line heights and spacing
- Provides exceptional readability
- Includes debug tools to maintain perfect alignment
- Supports both light and dark themes

You can toggle the debug grid by checking the "Debug grid" checkbox at the bottom of any page to see the underlying grid system.

## Advanced Usage

### Using HTML in Markdown
You can mix HTML and markdown for advanced layouts:

```markdown
# My Post Title

Regular markdown content here.

<div class="grid">
  <div class="width-auto">
    More **markdown** content in a grid column.
  </div>
  <div class="width-min">
    <button>Action</button>
  </div>
</div>

Back to regular markdown.
```

### Custom Components
The CSS provides building blocks for creating custom components:

- All spacing uses `var(--line-height)` units
- Colors use CSS custom properties for theme switching
- Interactive elements have consistent styling
- Everything respects the baseline grid

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

1. Write and edit posts directly in Reprose's online editor
2. Push changes to your repository
3. Watch as GitHub Actions automatically builds and deploys your blog

The frontmatter format is fully compatible with Reprose's standard fields (`title`, `description`, `date`) and supports any additional custom fields you want to add.

## Credits

The monospace design system is inspired by and adapted from [The Monospace Web](https://github.com/owickstrom/the-monospace-web/) by Oskar Wickström, which promotes the use of monospace fonts and strict typographic grids for web design. 