from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to True once working
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    # Fill username and password
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")

    # Click login
    page.click("button[type=submit]")

    # Wait for success message
    page.wait_for_selector(".flash.success")

    success_message = page.inner_text(".flash.success")
    print("Login result:", success_message)

    # Take screenshot of success
    page.screenshot(path="login_success.png")

    browser.close()
