from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://news.ycombinator.com")

    # Wait for content to load
    page.wait_for_selector("span.titleline")

    # Generate PDF with custom options
    page.pdf(
        path="hacker_news.pdf",
        format="A4",
        print_background=True,
        margin={"top": "20px", "bottom": "20px", "left": "20px", "right": "20px"},
        scale=0.8
    )
    print("PDF saved as hacker_news.pdf")

    browser.close()
