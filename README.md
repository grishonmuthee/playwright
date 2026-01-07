# playwright
Repo for Playwright python projects for CB Bot
Important Playwright Concepts & Functions (Python)Playwright's API is built around reliability with auto-waiting, locators, and cross-browser support. Here's a curated list of the most essential things to know and functions/methods, grouped logically (sync API focus).Core Structure & Lifecyclesync_playwright() — Entry point: Context manager to start Playwright.python

with sync_playwright() as p: ...

Browser launch — p.chromium.launch(headless=True/False), p.firefox.launch(), p.webkit.launch().
BrowserContext — Isolated session (cookies, storage): browser.new_context().
Page — Single tab: context.new_page() or browser.new_page().
Close order — Always close page → context → browser.

Key Locator Methods on Page (Recommended Selectors)These are user-facing, resilient, and auto-wait:bugbug.io

ikalamtech.com

codoid.com

Method
Description
Example
get_by_role(role, name=...)
By ARIA role (button, link, checkbox, etc.)
page.get_by_role("button", name="Submit").click()
get_by_text(text, exact=False)
By visible text content
page.get_by_text("Welcome").click()
get_by_label(text)
Form inputs by label text
page.get_by_label("Username").fill("user")
get_by_placeholder(text)
Inputs by placeholder
page.get_by_placeholder("Search...").fill("query")
get_by_alt_text(text)
Images by alt attribute
page.get_by_alt_text("Logo").click()
get_by_title(text)
By title attribute
page.get_by_title("Tooltip").hover()
get_by_test_id(id)
By data-testid (best for tests)
page.get_by_test_id("login-btn").click()
locator(selector)
Fallback CSS/XPath (less recommended)
page.locator("#id")

Important Locator Methods (Once You Have a Locator)Locators are chainable and preferred over direct page actions.azurestaticwebapps.dev

Category
Method
Description
Interaction
click(), dblclick(), hover(), fill(value), clear(), check(), uncheck(), press(key), type(text), select_option(), set_input_files()
Simulate user actions (auto-wait).
Querying
inner_text(), text_content(), inner_html(), get_attribute(name), input_value(), count(), bounding_box()
Get element data.
Filtering
filter(has_text=...), nth(index), first, last, all()
Narrow down multiple matches.
Waiting/State
wait_for(state="visible"), is_visible(), is_hidden(), is_enabled()
Check or wait for element state.

Navigation & Page MethodsMethod
Description
page.goto(url, wait_until="load")
Navigate (wait_until: "load", "domcontentloaded", "networkidle").
page.reload()
Reload page.
page.go_back()/go_forward()
History navigation.
page.title()
Get page title.
page.url
Current URL (property).
page.content()
Full HTML source.
page.screenshot(path=, full_page=True)
Capture image.
page.pdf(path=)
Generate PDF (Chromium only).

Waiting & EventsMethod
Description
page.wait_for_load_state(state="networkidle")
Wait for page load.
page.wait_for_selector(selector, state="visible")
Wait for element.
page.wait_for_timeout(ms)
Simple pause (avoid if possible).
page.wait_for_url(url)
Wait for URL change.
page.wait_for_event("load"/"popup"/etc.)
Wait for events.

Utilities & Advancedpage.evaluate("js code") → Run JS in page.
page.route("**/*", handler) → Intercept/modify network requests.
context.storage_state(path=) → Save/load cookies/session.
page.keyboard.press("Enter"), page.mouse.click(x,y) → Low-level input.
Tracing: context.tracing.start()/stop(path="trace.zip") for debugging.

Best Practices:Always use locators (get_by_*) over raw selectors.
Prefer fill() over type().
Use expect(locator).to_be_visible() for assertions (in tests).
Set timeouts: page.set_default_timeout(30000).

This covers 90% of daily use! For full reference: https://playwright.dev/python/docs/apiPractice with the examples from earlier—let me know what you want to dive deeper into next.

