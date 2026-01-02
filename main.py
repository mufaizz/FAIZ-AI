import asyncio
import sys
import time
import os
import shutil
import json
from datetime import datetime
sys.path.append('.')

from src.utils.spell_intent import QueryPreprocessor
from src.search.retriever import Retriever

def type_text(text, delay=0.03, end="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def center_text(text):
    cols = shutil.get_terminal_size().columns
    return text.center(cols)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def save_results(query, results):
    data = {
        "query": query,
        "timestamp": datetime.now().isoformat(),
        "total_files": len(results),
        "results": results
    }
    
    with open("faiz_results.json", 'w') as f:
        json.dump(data, f, indent=2)
    
    return "faiz_results.json"

async def main():
    clear_screen()
    
    type_text(center_text("FAIZ AI"), 0.02)
    type_text("\033[80CBy-Mufaiz", 0.02)
    type_text("―" * 100, 0.002)
    
    type_text("\nEnter search query: ", 0.02, end="")
    query = input()
    
    clear_screen()
    type_text(center_text("FAIZ AI"), 0.02)
    type_text("\033[80CBy-Mufaiz", 0.02)
    type_text("―" * 100, 0.02)
    
    type_text(f"\nSearching: {query}", 0.02)
    
    qp = QueryPreprocessor()
    rt = Retriever()
    
    clean_q, msg = qp.process(query)
    if msg:
        type_text(f"\n⚠️  {msg}", 0.01)
        time.sleep(2)
        return
    
    start_time = time.time()
    
    print("\n" + " " * 40 + "│")
    print(" " * 40 + "│")
    
    logs = []
    protocols = ["Google", "FTP Servers", "IPFS Network", "Torrent DHT", "Academic DB"]
    results = []
    
    for i in range(12):
        log = f"[{time.strftime('%H:%M:%S')}] Scanning {protocols[i % 5]}"
        logs.append(log)
        print(f"\033[K{log}")
        
        if len(logs) > 8:
            print(f"\033[{len(logs)+1}A", end="")
            for j in range(min(8, len(logs))):
                print(f"\033[K{logs[-(8-j)]}")
            print(f"\033[{min(8, len(logs))}B", end="")
        
        await asyncio.sleep(0.2)
        
        if i == 8:
            results = await rt.search(clean_q)
    
    print(" " * 40 + "│")
    print(" " * 40 + "│")
    
    ranked = await rt.rank(clean_q, results) if results else []
    
    elapsed = time.time() - start_time
    type_text(f"\n✅ Found {len(ranked)} files in {elapsed:.2f}s", 0.01)
    
    if ranked:
        save_file = save_results(clean_q, ranked)
        type_text(f"💾 Saved to: {save_file}", 0.01)
        
        print("\nTop results:")
        for i, url in enumerate(ranked[:8], 1):
            print(f"  {i}. {url}")
    
    print("\n" + "―" * 100)

if __name__ == "__main__":
    asyncio.run(main())