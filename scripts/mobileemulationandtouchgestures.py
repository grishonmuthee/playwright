from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_13 = p.devices["iPhone 13"]
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**iphone_13, locale="en-US", timezone_id="America/New_York")
    page = context.new_page()

    page.goto("https://www.apple.com/iphone/")
    print("Mobile page title:", page.title())

    # Simulate swipe up
    page.touchscreen.tap(x=200, y=600)
    page.mouse.down()
    page.mouse.move(200, 600)
    page.mouse.move(200, 200)  # Swipe up
    page.mouse.up()

    page.wait_for_timeout(1000)
    page.screenshot(path="iphone_emulation.png", full_page=True)
    context.close()
    browser.close()
