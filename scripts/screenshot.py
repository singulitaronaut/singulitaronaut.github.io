"""
Screenshot utility for capturing the blog homepage.
Takes a full-page screenshot of docs/index.html for README documentation.
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright  # type: ignore


def take_screenshot():
    """Take a full-page screenshot of the blog homepage."""
    
    # Get the workspace root directory
    workspace_root = Path(__file__).parent.parent
    
    # Path to the built HTML file
    html_file = workspace_root / "docs" / "index.html"
    
    if not html_file.exists():
        print(f"Error: {html_file} does not exist. Please build the site first with:")
        print("uv run scripts/build.py")
        sys.exit(1)
    
    # Output path for the screenshot
    screenshot_path = workspace_root / "screenshot.png"
    
    print(f"Taking screenshot of {html_file}")
    print(f"Saving to {screenshot_path}")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Set viewport size for consistent screenshots
        page.set_viewport_size({"width": 1200, "height": 800})
        
        # Navigate to the HTML file
        file_url = f"file://{html_file.absolute()}"
        page.goto(file_url)
        
        # Wait for any images to load
        page.wait_for_load_state("networkidle")
        
        # Take full page screenshot
        page.screenshot(path=str(screenshot_path))
        
        browser.close()
    
    print(f"Screenshot saved successfully to {screenshot_path}")
    return screenshot_path


if __name__ == "__main__":
    take_screenshot()