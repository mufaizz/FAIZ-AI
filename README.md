# FAIZ-AI — Master-level Universal File Search & Retrieval Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/mufaizz/FAIZ-AI/blob/main/LICENSE)

FAIZ-AI is a high-performance, asynchronous CLI tool for searching and retrieving files across multiple protocols (HTTP, FTP, IPFS, Torrent) in parallel. It combines semantic search with vector embeddings to return highly relevant results, and includes multiple safety layers such as intent verification, extension filtering, and VirusTotal hash checks.

License: MIT — see the [LICENSE](./LICENSE) file for full terms.

🚀 Key capabilities:
- Multi-protocol simultaneous search (HTTP, FTP, IPFS, Torrent)
- Semantic ranking using SentenceTransformer embeddings
- Asynchronous, non-blocking architecture (asyncio + aiohttp)
- Built-in safety: spell correction, intent verification, extension blocking, VirusTotal checks
- CLI-first design for speed and automation

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
- Fast and concurrent: fully asynchronous with careful use of connection pools, rate-limiting and timeouts.
- Safety-first: spell correction, malicious-intent filtering, extension blocking, and optional VirusTotal verification for file hashes.

---

## Features
- Multi-Protocol Search
  - HTTP: advanced targeted searching (file types, dorks)
  - FTP: asynchronous scanning of public FTP servers (e.g., FreeBSD mirrors, kernel.org)
  - IPFS: search via public IPFS gateways
  - Torrent: DHT-style discovery for magnets and .torrent metadata
- Semantic Ranking
  - Embeddings via `sentence-transformers` (configurable model)
- Smart Query Processing
  - Spell correction (pyspellchecker)
  - Intent verification to block malicious or unsafe queries
- Safety Verifiers
  - Extension filtering (block dangerous extensions like `.exe`, `.bat`, `.sh`)
  - VirusTotal integration for validating file hashes (optional; requires API key)
- Output
  - Real-time logs during scanning
  - Final ranked results saved to `faiz_results.json`

---

## Install

### Prerequisites
- Python 3.8+
- pip
- Linux/Unix environment recommended for automated script
- (Optional) VirusTotal API key if you want built-in VT checks

### Automated setup
The repository includes a setup script that will install system packages, create a virtual environment, and install dependencies.

```bash
chmod +x setup.sh
./setup.sh
```

> The script may run system package updates. Review the script before running if you prefer manual control.

### Manual setup
Clone the repository and create a virtual environment:

```bash
git clone https://github.com/mufaizz/FAIZ-AI.git
cd FAIZ-AI
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
# or (if no requirements file present)
pip install sentence-transformers==2.2.2 aiohttp==3.9.1 aioftp==0.21.3 pyspellchecker==0.7.2 pyyaml==6.0.1 numpy==1.24.3
```

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
  virus_total_api_key: ""   # optional, set to enable VirusTotal checks

ftp:
  public_servers:
    - "ftp.freebsd.org"
    - "ftp.kernel.org"
```

Adjust `config/config.yaml` to enable/disable protocols, change the model, or set safety policies.

---

## Usage

Activate the virtual environment (if not already active):

```bash
source venv/bin/activate
```

Run the CLI:

```bash
python main.py
```

Enter a query at the prompt, for example:
- `linux documentation pdf`
- `ubuntu iso torrent`

What happens:
- FAIZ-AI performs parallel searches across configured protocols.
- Candidates are embedded and ranked by semantic similarity to your query.
- Top results are printed and saved to `faiz_results.json`.
- If VirusTotal is configured, file hashes will be checked and flagged.

---

## Project structure

faiz-ai/
├── config/
│   └── config.yaml          # Configuration settings
├── src/
│   ├── agents/              # Headless browsing agents
│   ├── core/
│   │   └── semantic_brain.py # Vector embedding logic
│   ├── protocols/           # Protocol handlers (HTTP, FTP, IPFS, Torrent)
│   ├── safety/              # Safety verifiers (VirusTotal, hash checks)
│   ├── search/              # Main retriever and ranker logic
│   └── utils/               # Helpers (logger, spell check)
├── main.py                  # CLI entry point
├── setup.sh                 # Automated install & setup
├── requirements.txt         # Python dependencies (recommended)
└── README.md

---

## Safety & legal

FAIZ-AI is provided as an educational/personal project. Use responsibly and in accordance with applicable laws.

- Do not use FAIZ-AI to retrieve copyrighted material unless you have permission.
- The tool includes filters to block obviously malicious queries and dangerous file types, but protection is not guaranteed.
- Virus checks via VirusTotal are optional and require an API key; they do not replace thorough security review.

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

Summary: The MIT License is a permissive open-source license allowing reuse, modification, and distribution with attribution. If you want a short SPDX badge or a link to the canonical license text, I can add that as well:
- SPDX: `MIT`
- Canonical text: https://opensource.org/licenses/MIT

---

## Contact

Repository: [mufaizz/FAIZ-AI](https://github.com/mufaizz/FAIZ-AI)
