from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")

    # Use robust locators (text + role + chaining)
    quotes = page.locator("div.quote").filter(has_text="love").all()

    print(f"Found {len(quotes)} quotes containing 'love':")
    for quote in quotes:
        text = quote.locator("span.text").inner_text()
        author = quote.locator("small.author").inner_text()
        print(f"• \"{text}\" — {author}")

    # Click "Next" until disabled
    while page.locator("li.next > a").is_visible():
        page.click("li.next > a")
        page.wait_for_load_state("networkidle")

    print("Reached end of pagination")
    browser.close()
