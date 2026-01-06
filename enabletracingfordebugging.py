from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="/tmp/playwright-temp",
        headless=False,
        record_video_dir="videos/",  # Optional: saves video
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://example.com")
    page.fill("input[name='q']", "test")  # Simulate action

    context.tracing.stop(path="trace.zip")
    print("Trace saved as trace.zip — open at https://trace.playwright.dev")

    context.close()
