from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://infinite-scroll.com/demo/full-page/")

    # Auto-scroll to bottom repeatedly until no new content loads
    items = set()
    last_height = page.evaluate("() => document.body.scrollHeight")

    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)  # Wait for new content

        new_height = page.evaluate("() => document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract all item texts
    texts = page.locator("div.item p").all_inner_texts()
    print(f"Loaded {len(texts)} items:")
    for text in texts[:10]:  # Show first 10
        print("-", text)
    print("...")

    page.screenshot(path="infinite_scroll.png", full_page=True)
    browser.close()
