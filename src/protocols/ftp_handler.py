from ftplib import FTP
import asyncio
import aioftp

class FTPHandler:
    def __init__(self, timeout=30):
        self.timeout = timeout
        self.public_servers = [
            ('ftp.freebsd.org', 21, 'anonymous', ''),
            ('speedtest.tele2.net', 21, 'anonymous', ''),
            ('ftp.ncbi.nlm.nih.gov', 21, 'anonymous', ''),
            ('mirrors.kernel.org', 21, 'anonymous', ''),
            ('ftp.gnu.org', 21, 'anonymous', '')
        ]

    async def search_public_servers(self, filename_pattern=None):
        all_files = []
        for host, port, user, passwd in self.public_servers:
            try:
                files = await self.list_files_async(host, port, user, passwd)
                if filename_pattern:
                    files = [f for f in files if filename_pattern.lower() in f.lower()]
                all_files.extend([f"ftp://{host}:{port}/{f}" for f in files[:10]])
            except:
                continue
        return all_files

    async def list_files_async(self, host, port=21, username='anonymous', password=''):
        files = []
        try:
            async with aioftp.Client.context(host, port, username, password) as client:
                async for path, info in client.list(recursive=True):
                    if info['type'] == 'file':
                        files.append(path)
                        if len(files) >= 50:
                            break
        except:
            pass
        return files

    def search_files_sync(self, host):
        return self.search_public_servers()