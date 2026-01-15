from seleniumbase import SB
from playwright.sync_api import sync_playwright

# 1. Initialize SeleniumBase with UC Mode and Xvfb for headless Linux bypass
with SB(uc=True, xvfb=True, locale="en") as sb:
    url = "https://www.bing.com/turing/captcha/challenge"
    
    print("Opening target with UC Mode...")
    # Open the URL with a specialized redirect/reconnect for higher stealth
    sb.uc_open_with_reconnect(url, 4)
    sb.sleep(2)

    # 2. Use specialized GUI-based captcha solving
    # Standard headless mode fails here; Xvfb allows these methods to work.
    print("Solving CAPTCHA via GUI-based click...")
    try:
        # Tries to handle common CAPTCHA types automatically
        sb.solve_captcha()
    except Exception:
        # Fallback for complex 'Click-to-verify' challenges
        sb.uc_gui_click_captcha()
    
    sb.sleep(5)

    # 3. Connect Playwright to the active, solved session
    # Retrieve the remote-debugging-port from the SeleniumBase driver service
    port = sb.driver.service.port
    endpoint_url = f"http://localhost:{port}"

    print(f"Connecting Playwright to {endpoint_url}...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        # Inherit the page where the CAPTCHA was just solved
        page = browser.contexts[0].pages[0]

        print("Capturing full-page screenshot via Playwright...")
        page.screenshot(path="bing_solved_xvfb.png", full_page=True)
        print("Success! Screenshot saved as 'bing_solved_xvfb.png'.")

# Browser and Xvfb display close automatically at the end of the 'with' block
