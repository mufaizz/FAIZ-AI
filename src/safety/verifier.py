import hashlib
import aiohttp

class SafetyVerifier:
    def __init__(self):
        self.virus_total_key = None

    def calculate_hash(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path,"rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    async def check_virustotal(self, file_hash):
        if not self.virus_total_key:
            return None
        url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
        headers = {"x-apikey": self.virus_total_key}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as resp:
                    if resp.status == 200:
                        return await resp.json()
        except:
            pass
        return None

    def is_safe_extension(self, filename):
        safe_ext = {'.pdf', '.txt', '.docx', '.xlsx', '.jpg', '.png', '.mp4', '.mp3'}
        return any(filename.lower().endswith(ext) for ext in safe_ext)