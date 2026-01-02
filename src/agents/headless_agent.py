import asyncio
from pyppeteer import launch

class HeadlessAgent:
    def __init__(self):
        self.browser = None
        self.page = None

    async def start(self):
        self.browser = await launch(headless=True, args=['--no-sandbox'])
        self.page = await self.browser.newPage()

    async def stop(self):
        if self.browser:
            await self.browser.close()

    async def search_form(self, url, form_data):
        if not self.browser:
            await self.start()
        await self.page.goto(url)
        for selector, value in form_data.items():
            await self.page.type(selector, value)
        await self.page.keyboard.press('Enter')
        await asyncio.sleep(3)
        content = await self.page.content()
        return content

    async def extract_download_links(self, html):
        import re
        links = re.findall(r'href=["\'](.*?\.(pdf|docx?|txt|zip))["\']', html, re.I)
        return [link[0] for link in links]