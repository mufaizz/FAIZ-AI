#!/bin/bash
set -e  # Exit on any error

echo "Setting up FAIZ AI development environment..."

# Update package list
sudo apt-get update -y

# 1. Install System Dependencies
echo "Installing system dependencies..."
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    curl \
    git \
    pkg-config \
    libssl-dev

# 2. Install Python & Virtual Environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install core Python packages
echo "Installing Python packages..."
pip install --upgrade pip
pip install \
    sentence-transformers \
    fastapi \
    uvicorn \
    pydantic \
    requests \
    aiofiles \
    python-magic \
    pyyaml \
    pytest \
    pyspellchecker \
    pyppeteer \
    aioftp \
    aiohttp \
    bencodepy \
    sentence-transformers

# 5. Install Node.js & npm (for headless browser agents)
echo "Installing Node.js..."
sudo apt-get install -y nodejs
sudo apt-get install -y nsolid -y

# 6. Create essential config file
echo "Creating default configuration..."
cat > config/config.yaml << EOF
cat > /workspaces/FAIZ-AI/config/config.yaml << 'EOF'
# FAIZ AI Configuration
core:
  model: "all-MiniLM-L6-v2"
  embedding_dim: 384

search:
  timeout: 30
  max_results: 50
  protocols: ["http", "ftp", "ipfs", "torrent"]

safety:
  enable_verification: false  # Phase 1
  max_file_size_mb: 100
EOF

echo "Setup complete."
echo "To activate the environment, run: source venv/bin/activate"