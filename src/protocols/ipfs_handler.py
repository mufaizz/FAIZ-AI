import aiohttp
import asyncio

class IPFSHandler:
    def __init__(self, gateway="https://ipfs.io/ipfs/"):
        self.gateway = gateway
        self.timeout = 30

    async def search_cid(self, cid):
        try:
            url = f"{self.gateway}{cid}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=self.timeout) as resp:
                    if resp.status == 200:
                        return url
        except:
            pass
        return None

    async def find_files(self, query, max_results=10):
        search_urls = [
            f"https://ipfs-search.com/api/v1/search?q={query}&type=file",
            f"https://dweb.link/api/v0/search?q={query}"
        ]
        results = []
        for url in search_urls:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=self.timeout) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            if 'hash' in data:
                                results.append(f"ipfs://{data['hash']}")
            except:
                continue
        return results[:max_results]