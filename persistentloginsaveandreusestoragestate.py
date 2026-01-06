from playwright.sync_api import sync_playwright
import os

STATE_FILE = "auth_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Run headed first time for manual login if needed

    if os.path.exists(STATE_FILE):
        # Reuse saved session
        context = browser.new_context(storage_state=STATE_FILE)
        print("Logged in using saved session")
    else:
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type=submit]")
        page.wait_for_selector(".flash.success")
        print("Logged in manually")

        # Save cookies/localStorage for future runs
        context.storage_state(path=STATE_FILE)

    # Now use the authenticated context
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure")
    print("Secure area title:", page.title())
    page.screenshot(path="authenticated_page.png")

    context.close()
    browser.close()
