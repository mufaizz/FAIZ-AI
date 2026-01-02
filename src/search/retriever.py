from src.core.semantic_brain import SemanticBrain
from src.protocols.http_handler import HTTPHandler
from src.protocols.ftp_handler import FTPHandler
from src.protocols.ipfs_handler import IPFSHandler
from src.protocols.torrent_handler import TorrentHandler
import asyncio

class Retriever:
    def __init__(self):
        self.brain = SemanticBrain()
        self.http = HTTPHandler()
        self.ftp = FTPHandler()
        self.ipfs = IPFSHandler()
        self.torrent = TorrentHandler()

    async def search(self, query, filetypes=None):
        all_results = []
        
        # HTTP Search with timeout
        try:
            http_task = asyncio.create_task(self.http.search_files(query, filetypes))
            http_results = await asyncio.wait_for(http_task, timeout=20)
            all_results.extend(http_results)
        except:
            pass
        
        # FTP Search with timeout
        try:
            ftp_task = asyncio.create_task(self.ftp.search_public_servers())
            ftp_results = await asyncio.wait_for(ftp_task, timeout=15)
            all_results.extend(ftp_results[:10])
        except:
            pass
        
        # IPFS Search
        try:
            ipfs_results = await self.ipfs.find_files(query)
            all_results.extend(ipfs_results)
        except:
            pass
        
        # Torrent Search
        try:
            torrent_results = await self.torrent.search_dht(query)
            all_results.extend(torrent_results)
        except:
            pass
        
        return all_results[:50]

    async def rank(self, query, results):
        if not results:
            return []
        
        query_embed = self.brain.get_embedding(query)
        scored = []
        
        for result in results:
            try:
                result_text = result.split('/')[-1]
                result_embed = self.brain.get_embedding(result_text)
                score = self.brain.similarity(query_embed, result_embed)
                scored.append((score, result))
            except:
                scored.append((0.1, result))
        
        scored.sort(key=lambda x: x[0], reverse=True)
        return [url for _, url in scored]