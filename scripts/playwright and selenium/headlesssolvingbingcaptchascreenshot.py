from seleniumbase import sb_cdp
from playwright.sync_api import sync_playwright

# 1. Launch SeleniumBase in Headless CDP Mode
# Pure CDP mode (sb_cdp) doesn't use WebDriver, making it highly stealthy.
# For 2026, 'headless=True' is optimized for bot-detection bypass.
sb = sb_cdp.Chrome(headless=True, locale="en")

try:
    target_url = "https://www.bing.com/turing/captcha/challenge"
    print(f"Opening {target_url} with SeleniumBase...")
    sb.get(target_url)
    sb.sleep(2)

    # 2. Use SeleniumBase's specialized CAPTCHA solver
    # This identifies and interacts with the challenge automatically.
    print("Solving CAPTCHA...")
    sb.solve_captcha()
    sb.sleep(3)

    # 3. Connect Playwright to the existing SeleniumBase session
    # This allows Playwright to 'inherit' the solved session state.
    endpoint_url = sb.get_endpoint_url()
    
    with sync_playwright() as p:
        # Attach to the browser using the remote debugging port
        browser = p.chromium.connect_over_cdp(endpoint_url)
        context = browser.contexts[0]
        page = context.pages[0]

        print("Capturing full-page screenshot via Playwright...")
        # Playwright's full_page parameter handles all scrolling/stitching internally.
        page.screenshot(path="full_page_headless2.png", full_page=True)
        print("Success! Screenshot saved as 'full_page_headless2.png'.")

finally:
    # 4. Proper cleanup for the CDP session.
    sb.driver.stop()
