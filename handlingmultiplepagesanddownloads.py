from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    
    # Set download path
    download_path = os.path.abspath("downloads")
    os.makedirs(download_path, exist_ok=True)
    context = browser.new_context(accept_downloads=True)

    page = context.new_page()
    page.goto("https://httpbin.org/image/png")

    # Start waiting for download before clicking
    with context.expect_download() as download_info:
        page.click("text=Click to download")  # This site doesn't have text, just demo logic
    # For real sites, replace with actual trigger, e.g., page.click("a:has-text('Download')")

    # Alternative: direct download from a known link
    page.goto("https://httpbin.org/bytes/10240")  # 10KB random data

    browser.close()
