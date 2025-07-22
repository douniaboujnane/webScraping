from playwright.async_api import Playwright, Browser, Page

async def launch_browser(p: Playwright) -> tuple[Browser, Page]:
    browser = await p.chromium.launch(headless=False)
    page = await browser.new_page()
    return browser, page

async def close_browser(browser: Browser):
    await browser.close()

