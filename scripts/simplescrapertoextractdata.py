from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://httpbin.org/json")

    # Extract JSON content as text
    content = page.inner_text("pre")
    print("JSON response:\n", content)

    # Or evaluate JavaScript to parse it
    data = page.evaluate("() => JSON.parse(document.querySelector('pre').textContent)")
    print("Parsed slides count:", len(data["slideshow"]["slides"]))

    browser.close()
