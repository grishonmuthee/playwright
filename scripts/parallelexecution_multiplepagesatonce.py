from playwright.sync_api import sync_playwright

def scrape_site(url, filename):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")  # Wait until no network activity
        print(f"{url} -> {page.title()}")
        page.screenshot(path=filename, full_page=True)
        browser.close()

# Run multiple in parallel using threads
from concurrent.futures import ThreadPoolExecutor

sites = [
    ("https://python.org", "python_org.png"),
    ("https://playwright.dev/python", "playwright_docs.png"),
    ("https://github.com", "github.png"),
]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(lambda args: scrape_site(*args), sites)

print("All sites scraped in parallel!")
