import asyncio
import random
from playwright.async_api import async_playwright

BASE_MESSAGE = "❤️🙏🏻 stake 🆔 Priyathakur23 😘❤️ Ganpati bappa moriya"

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()

        print("Starting Kick Bot...")
        await page.goto("https://kick.com/amitcbtf37")
        await page.wait_for_timeout(5000)

        while True:
            try:
                chat_input = page.locator('div#message-input, div[contenteditable="true"]').first
                if await chat_input.is_visible():
                    random_num = random.randint(100, 999)
                    final_msg = f"{BASE_MESSAGE} "

                    await chat_input.fill(final_msg)
                    await page.keyboard.press("Enter")
                    print(f"Sent: {final_msg}")

                # Exact 6.5 seconds delay
                await asyncio.sleep(4)

            except Exception as e:
                print(f"Error: {e}")
                await asyncio.sleep(4)

if __name__ == "__main__":
    asyncio.run(run_bot())
