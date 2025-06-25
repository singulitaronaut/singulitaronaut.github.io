# The Monospace Blog

A Python-powered Markdown blog based on [my Python replication](https://github.com/chriscarrollsmith/monospace-web-python) of [The Monospace Web](https://github.com/owickstrom/the-monospace-web) by Oskar Wickström. 

## Quick Start

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install Python 3.13+ and other dependencies with uv:
   ```bash
   uv sync
   ```

3. Edit your landing page in `posts/index.md`

4. Edit your blog posts in `posts/`

5. Build the site:
   ```bash
   uv run scripts/build.py
   ```

6. Open `dist/index.html` in a web browser to preview the site.

## Deployment to GitHub Pages

A Github workflow is configured to automatically build the site in the `dist` folder and commit and push the built files to the remote whenever you push source file changes to `main`.

You will need to enable GitHub Pages for your repository and configure Github Pages to serve the site from the `dist` folder on `main`. You can find these settings in the repository's `Settings > Pages > Build and deployment` section.

## Compatibility with Reprose

This blog generator is designed to work seamlessly with [Reprose](https://repose.pp.ua), an online markdown editor that integrates with GitHub. You can:

1. Write and edit posts directly in Reprose's online editor
2. Push changes to your repository with a button-click
3. Watch as GitHub Actions automatically builds and deploys your blog
4. The frontmatter format is fully compatible with Reprose's standard fields (title, description, date) and supports any additional custom fields you want to add.

## License

MIT License - see [LICENSE](LICENSE) for details.
