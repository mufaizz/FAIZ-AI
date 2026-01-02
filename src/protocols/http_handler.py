import aiohttp
import asyncio
from urllib.parse import quote_plus
import re

class HTTPHandler:
    def __init__(self, timeout=30):
        self.timeout = timeout
        self.session = None
        self.search_engines = {
            'google': 'https://www.google.com/search?q={query}+filetype:{ext}&num=20',
            'duckduckgo': 'https://html.duckduckgo.com/html/?q={query}+filetype:{ext}'
        }
        self.file_patterns = {
            'pdf': r'\.pdf(\?|$)',
            'doc': r'\.(doc|docx)(\?|$)',
            'video': r'\.(mp4|avi|mov|mkv|webm)(\?|$)',
            'audio': r'\.(mp3|wav|flac|aac)(\?|$)',
            'archive': r'\.(zip|rar|7z|tar|gz)(\?|$)'
        }

    async def start(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )

    async def stop(self):
        if self.session:
            await self.session.close()

    async def google_dork_search(self, query, filetype='pdf', max_results=10):
        if not self.session:
            await self.start()
        
        search_url = self.search_engines['google'].format(
            query=quote_plus(query),
            ext=filetype
        )
        
        try:
            async with self.session.get(search_url, timeout=10) as response:
                if response.status != 200:
                    return []
                html = await response.text()
                
            links = []
            patterns = [
                r'<a href="\/url\?q=(.*?)&',
                r'<a class=".*?" href="(http.*?\.{})'.format(filetype),
                r'href="(https?:\/\/[^"]*?\.{}[^"]*?)"'.format(filetype)
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, html, re.IGNORECASE)
                for match in matches:
                    if 'google.com' not in match and 'webcache' not in match:
                        links.append(match)
            
            return list(set(links))[:max_results]
            
        except Exception as e:
            return []

    async def search_files(self, query, filetypes=None, max_per_type=5):
        if filetypes is None:
            filetypes = ['pdf', 'doc', 'docx']
        
        all_files = []
        for ft in filetypes:
            files = await self.google_dork_search(query, ft, max_per_type)
            all_files.extend(files)
            await asyncio.sleep(0.5)
        
        return all_files