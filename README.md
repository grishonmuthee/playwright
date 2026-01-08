# Playwright (Python)

This repository serves as a reference and playground for using **Playwright with Python**, focusing on reliable browser automation using modern best practices.

* Playwright Python

* Browser automation

* Web automation

* End-to-end testing (E2E)

* Playwright sync API

* Cross-browser testing

Locators & best practices
---

## Core Playwright Concepts (Python – Sync API)

Playwright’s API is built around **auto-waiting**, **locators**, and **cross-browser support**.

### Lifecycle & Core Structure

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
```

**Key Components**

* **`sync_playwright()`** – Entry point (context manager)
* **Browser** – `p.chromium.launch()`, `p.firefox.launch()`, `p.webkit.launch()`
* **BrowserContext** – Isolated session (cookies, storage)
* **Page** – Single browser tab

**Close order (important):**

1. Page
2. Context
3. Browser

---

## Recommended Locator Methods (Best Practice)

Playwright locators are **resilient, user-facing, and auto-waiting**.

| Method                           | Description                    | Example                                              |
| -------------------------------- | ------------------------------ | ---------------------------------------------------- |
| `get_by_role(role, name=...)`    | By ARIA role                   | `page.get_by_role("button", name="Submit").click()`  |
| `get_by_text(text, exact=False)` | By visible text                | `page.get_by_text("Welcome").click()`                |
| `get_by_label(text)`             | Input by label                 | `page.get_by_label("Username").fill("user")`         |
| `get_by_placeholder(text)`       | Input by placeholder           | `page.get_by_placeholder("Search...").fill("query")` |
| `get_by_alt_text(text)`          | Image by alt text              | `page.get_by_alt_text("Logo").click()`               |
| `get_by_title(text)`             | Title attribute                | `page.get_by_title("Tooltip").hover()`               |
| `get_by_test_id(id)`             | `data-testid` (best for tests) | `page.get_by_test_id("login-btn").click()`           |
| `locator(selector)`              | CSS/XPath fallback             | `page.locator("#id")`                                |

---

## Locator Actions & Methods

Once you have a locator, you can chain actions and queries.

### Interaction

```python
locator.click()
locator.fill("value")
locator.hover()
locator.check()
locator.uncheck()
locator.press("Enter")
locator.select_option("option")
```

### Querying

```python
locator.inner_text()
locator.text_content()
locator.get_attribute("href")
locator.input_value()
locator.count()
locator.bounding_box()
```

### Filtering

```python
locator.filter(has_text="Admin")
locator.nth(0)
locator.first
locator.last
```

### Waiting & State

```python
locator.wait_for(state="visible")
locator.is_visible()
locator.is_hidden()
locator.is_enabled()
```

---

##  Navigation & Page Methods

| Method                                   | Description                  |
| ---------------------------------------- | ---------------------------- |
| `page.goto(url, wait_until="load")`      | Navigate to URL              |
| `page.reload()`                          | Reload page                  |
| `page.go_back()` / `page.go_forward()`   | History navigation           |
| `page.title()`                           | Get page title               |
| `page.url`                               | Current URL                  |
| `page.content()`                         | Full HTML                    |
| `page.screenshot(path=, full_page=True)` | Screenshot                   |
| `page.pdf(path=)`                        | Generate PDF (Chromium only) |

---

##  Waiting & Events

| Method                                              | Description                   |
| --------------------------------------------------- | ----------------------------- |
| `page.wait_for_load_state("networkidle")`           | Wait for load                 |
| `page.wait_for_selector(selector, state="visible")` | Wait for element              |
| `page.wait_for_timeout(ms)`                         | Hard wait (avoid if possible) |
| `page.wait_for_url(url)`                            | Wait for URL change           |
| `page.wait_for_event("popup")`                      | Wait for browser event        |

---

##  Utilities & Advanced Usage

```python
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
```

* **Network interception**

```python
page.route("**/*", handler)
```

* **Save / load session**

```python
context.storage_state(path="state.json")
```

* **Low-level input**

```python
page.keyboard.press("Enter")
page.mouse.click(100, 200)
```

* **Tracing (debugging)**

```python
context.tracing.start()
context.tracing.stop(path="trace.zip")
```

---

##  Best Practices

* Always use **locators (`get_by_*`)** over raw selectors
* Prefer `fill()` over `type()`
* Use assertions:

```python
from playwright.sync_api import expect
expect(locator).to_be_visible()
```

* Set global timeouts:

```python
page.set_default_timeout(30000)
```

---

## Resources

* Official Docs: [https://playwright.dev/python/docs/api](https://playwright.dev/python/docs/api)

---

