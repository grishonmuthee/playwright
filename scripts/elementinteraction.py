from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")

    # Accept cookies if the banner appears (Google sometimes shows it)
    if page.is_visible("text=Accept all"):
        page.click("text=Accept all")

    # Type into search box and submit
    page.fill('textarea[name="q"]', "Playwright Python")
    page.press('textarea[name="q"]', "Enter")

    # Wait for results and check title
    page.wait_for_selector("h3")  # Wait for search results
    print("Search results page title:", page.title())

    # Assert we're on the results page
    assert "Playwright Python" in page.title()

    browser.close()
    print("Test passed!")

