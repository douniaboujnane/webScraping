from playwright.async_api import Page
from .config import PAGE_TIME_OUT, SELECTORS

async def handle_cookie_banner(page: Page):
    try:
        await page.wait_for_selector(SELECTORS['popUp'], timeout=3000)
        await page.locator(SELECTORS['closePopUp']).click(timeout=3000)
        print("✅ Cookie banner closed.")
    except:
        print("ℹ️ No cookie banner detected.")


async def navigate_to_url(page: Page, url: str):
    await page.goto(url, timeout=PAGE_TIME_OUT)
    await handle_cookie_banner(page)


async def go_to_next_page(page: Page) -> bool:
    next_button = page.locator(SELECTORS['nextButton'])
    next_button_disabled = page.locator(SELECTORS['nextButtonDisabled'])
    
    if await next_button.count() > 0:
        print("→ Going to next page...")
        await next_button.click()
      #  await page.wait_for_timeout(1500)  
       # await page.wait_for_selector(SELECTORS['cards']['container'])  # Attendre rechargement
        return True
    elif await next_button_disabled.count() > 0:
        print("ℹ️ No more pages to navigate.")
        await page.wait_for_timeout(1500)
        return False
    else:
        print("✅ Next button not found.")
        return False
