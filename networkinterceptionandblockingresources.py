from playwright.sync_api import sync_playwright

def handle_route(route):
    # Block images, CSS, fonts to speed up loading
    if route.request.resource_type in ["image", "stylesheet", "font"]:
        route.abort()
    else:
        route.continue_()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Block unnecessary resources
    page.route("**/*", handle_route)

    page.goto("https://news.ycombinator.com")
    print("Hacker News title:", page.title())
    print("Page loaded faster without images/CSS!")

    page.screenshot(path="hn_no_images.png", full_page=True)
    browser.close()
