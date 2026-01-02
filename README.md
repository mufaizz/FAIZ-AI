# FAIZ-AI — > It is an interactive CLI-based AI search engine.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/mufaizz/FAIZ-AI/blob/main/LICENSE)

FAIZ-AI is an asynchronous CLI tool for searching and retrieving files across multiple protocols (HTTP, FTP, IPFS, Torrent) in parallel. It combines semantic search with vector embeddings to rank candidate results.

License: MIT — see the [LICENSE](./LICENSE) file for full terms.

🚀 Key capabilities:
- Multi-protocol simultaneous search (HTTP, FTP, IPFS, Torrent)
- Semantic ranking using SentenceTransformer embeddings
- Asynchronous, non-blocking architecture (asyncio + aiohttp)
- Built-in safety measures: spell correction, intent verification, extension blocking
- CLI-first design for automation and scripting

---

## Table of contents
- [Highlights](#highlights)
- [Features](#features)
- [Install](#install)
  - [Prerequisites](#prerequisites)
  - [Automated setup](#automated-setup)
  - [Manual setup](#manual-setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project structure](#project-structure)
- [Safety & legal](#safety--legal)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Highlights
- Multi-protocol aggregator: query HTTP (including Google dorking for file types), public FTP servers, IPFS gateways, and Torrent DHT-like discovery simultaneously.
- Semantic intelligence: uses `sentence-transformers` (default model `all-MiniLM-L6-v2`) to embed queries and candidate results, ranking by semantic similarity rather than raw keyword matches.
- Asynchronous design with connection pools, rate-limiting and timeouts to support concurrent operations.
- Safety-focused: includes basic safeguards such as spell correction, intent filtering and extension blocking; these do not guarantee safety and should not be considered a replacement for careful review.

---

## Features
- Multi-Protocol Search
  - HTTP: targeted searching (file types, dorks)
  - FTP: asynchronous scanning of public FTP servers (e.g., FreeBSD mirrors, kernel.org)
  - IPFS: search via public IPFS gateways
  - Torrent: DHT-style discovery for magnets and .torrent metadata
- Semantic Ranking
  - Embeddings via `sentence-transformers` (configurable model)
- Smart Query Processing
  - Spell correction (pyspellchecker)
  - Intent verification to block malicious or unsafe queries
- Safety Verifiers
  - Extension filtering (recommend blocking dangerous extensions like `.exe`, `.bat`, `.sh`)
- Output
  - Real-time logs during scanning
  - Final ranked results saved to `faiz_results.json`

---

## Install

### Prerequisites
- Python 3.8+
- pip
- Linux/Unix environment recommended for automated script

### Setup and Usage
1. Clone Repository or Download ZIP.
Open Terminal and
Paste This:
```
git clone https://github.com/mufaizz/FAIZ-AI.git
```
2. Make `setup.sh` executable.
Type:
```
chmod +x setup.sh
```
3. Run `setup.sh`.
```
sudo bash setup.sh
```
<img width="527" height="51" alt="oie_1Hbw91JKkt13" src="https://github.com/user-attachments/assets/ec2e30c1-1d35-4102-8039-75d4398bc3d8" />


4. Activate Environment.
```
source venv/bin/activate
```


<img width="569" height="36" alt="oie_PrKev1XF86d1" src="https://github.com/user-attachments/assets/c9d7ffd8-0d67-4e6b-937c-1aed5e49a55f" />

5. Run `main.py`.
```
python main.py
```


<img width="562" height="52" alt="oie_MRveXXCQyxtN" src="https://github.com/user-attachments/assets/e2e301d8-2b68-4076-94df-e2bac7752b27" />

6. Enter a query at the prompt, for example:

<img width="851" height="137" alt="oie_r5S7GejDZqfN" src="https://github.com/user-attachments/assets/f3893ddd-5b5c-472a-b200-c15af9ae7dae" />

7. Running Interface:

<img width="759" height="274" alt="oie_39wRwc9y7N9y" src="https://github.com/user-attachments/assets/569dbf06-9ac7-47af-b5a0-22f4b3b94062" />


8. Final Results:

<img width="759" height="274" alt="oie_39wRwc9y7N9y" src="https://github.com/user-attachments/assets/68c18fba-9b5c-4390-9ded-d87d37308b85" />


What happens:
- FAIZ-AI performs parallel searches across configured protocols.
- Candidates are embedded and ranked by semantic similarity to your query.
- Top results are printed and saved to `faiz_results.json`.


---

## Configuration

All runtime configuration lives in `config/config.yaml`. Example configuration (trimmed):

```yaml
core:
  model: "all-MiniLM-L6-v2"    # SentenceTransformer model
  timeout: 60                  # global search timeout in seconds

protocols:
  active: ["http", "ftp", "ipfs", "torrent"]

filetypes:
  http: ["pdf", "docx", "txt", "mp4", "iso"]

safety:
  blocked_extensions: [".exe", ".bat", ".sh"]

ftp:
  public_servers:
    - "ftp.freebsd.org"
    - "ftp.kernel.org"
```

Adjust `config/config.yaml` to enable/disable protocols, change the model, or set safety policies.

---


## Safety & legal

FAIZ-AI is provided as an educational/personal project. Use responsibly and in accordance with applicable laws.
## ⚠️ Disclaimer

FAIZ-AI is intended for educational and research purposes only.
The author is not responsible for misuse or access to illegal or copyrighted material.
Always follow local laws and ethical guidelines.


- Do not use FAIZ-AI to retrieve copyrighted material unless you have permission.
- The tool includes filters and safeguards, but protection is not guaranteed — review and verify results as appropriate.
- The project does not provide guarantees about the safety or legality of retrieved files.

---

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a feature branch (e.g., `feat/ipfs-improvements`).
3. Add tests where applicable.
4. Open a pull request describing the change.

Please keep changes focused and well-documented. If you want help drafting issues or breaking large features into tasks, open an issue describing your idea.

---

## License

This repository is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## Contact

Repository: [mufaizz/FAIZ-AI](https://github.com/mufaizz/FAIZ-AI)
