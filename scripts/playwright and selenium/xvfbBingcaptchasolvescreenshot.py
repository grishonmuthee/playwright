# Xvfb (X virtual framebuffer) is an X server that performs all graphical operations in virtual memory without displaying any screen output.
# It does not require a physical display or input device.
# This makes it ideal for running GUI applications on "headless" systems (computers without monitors, keyboards, or mice), such as servers used for automated testing or batch processing.
from seleniumbase import sb_cdp
from playwright.sync_api import sync_playwright

# 1. Use xvfb=True instead of headless=True for Linux environments.
# This runs a 'regular' browser in a virtual display, making it undetectable.
# On Windows/macOS, you may still need headless=False for CAPTCHA solving.
sb = sb_cdp.Chrome(xvfb=True, headless=True, locale="en") 

try:
    url = "https://www.bing.com/turing/captcha/challenge"
    print(f"Opening {url} via SeleniumBase...")
    sb.get(url)
    sb.sleep(5)

    # 2. Use specialized UC-mode solving methods
    # solve_captcha() is the general method; uc_gui_click_captcha() is 
    # specifically for 'click-to-verify' challenges that require a GUI.
    print("Solving CAPTCHA...")
    try:
        sb.solve_captcha() 
    except Exception:
        # Fallback for specific GUI-based challenges
        sb.uc_gui_click_captcha() 
    
    sb.sleep(5)

    # 3. Connect Playwright to the stealthy, solved session
    endpoint_url = sb.get_endpoint_url()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        # Use the existing page where the CAPTCHA was solved
        page = browser.contexts[0].pages[0]

        print("Capturing full-page screenshot...")
        page.screenshot(path="xvfb_headless_solved_captcha_full.png", full_page=True)
        print("Screenshot saved: xvfb_headless_solved_captcha_full.png")

finally:
    sb.driver.stop()
