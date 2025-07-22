import asyncio
from playwright.async_api import async_playwright
from scraping.config import URL, SELECTORS
from scraping.browser import launch_browser, close_browser
from scraping.navigation import go_to_next_page, navigate_to_url
from scraping.extract import extract_data_from_page
from scraping.save import save_data_to_csv

async def main():
    print("Starting scrape...")
    async with async_playwright() as p:
        all_data = []
        browser, page = await launch_browser(p)
        await navigate_to_url(page, URL)

        await page.wait_for_selector(SELECTORS['zone'])
        
        result = await page.locator(SELECTORS['resultCount']).nth(0).text_content()
        print(f"{result} propriétés trouvées.")

        while True:
            await page.wait_for_selector(SELECTORS['resultContainer'])
            cards_data = await extract_data_from_page(page)
            all_data.extend(cards_data)

            has_next = await go_to_next_page(page)
            if not has_next:
                break

        await close_browser(browser)

asyncio.run(main())
