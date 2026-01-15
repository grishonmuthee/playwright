from seleniumbase import sb_cdp
from playwright.sync_api import sync_playwright

# 1. Start SeleniumBase CDP Mode
# This launches Chrome with the correct remote-debugging-port automatically
sb = sb_cdp.Chrome(headless=True)

try:
    url = "https://abrahamjuliot.github.io/creepjs/"
    sb.get(url)
    sb.sleep(10)  # Let SeleniumBase handle initial stealth/loading

    # 2. Get the CDP Endpoint URL from SeleniumBase
    cdp_url = sb.get_endpoint_url()

    # 3. Use Playwright to connect to the same browser session
    with sync_playwright() as p:
        # Connect over the CDP endpoint provided by SeleniumBase
        browser = p.chromium.connect_over_cdp(cdp_url)
        context = browser.contexts[0]
        page = context.pages[0]

        print("Playwright successfully attached to SeleniumBase browser.")
        
        # 4. Use Playwright's superior screenshot engine
        page.screenshot(path="full_headless_playwrightandcdp.png", full_page=True)
        print("Full-page screenshot saved via Playwright.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cleanup: Close SeleniumBase (which also closes the browser)
    sb.driver.stop()
