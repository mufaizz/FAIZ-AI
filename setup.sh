#!/bin/bash
set -e

echo "FAIZ AI - Complete System Setup"
echo "================================"

# Update system
sudo apt-get update -y

# Install Python and essentials
sudo apt-get install -y python3 python3-pip python3-venv curl

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all required Python packages
pip install --upgrade pip
pip install sentence-transformers==2.2.2
pip install aiohttp==3.9.1
pip install aioftp==0.21.3
pip install pyspellchecker==0.7.2
pip install pyyaml==6.0.1
pip install numpy==1.24.3
pip install bencodepy
pip install pyppeteer

# Create essential config if not exists
mkdir -p config
cat > config/config.yaml << 'EOF'
core:
  model: "all-MiniLM-L6-v2"

search:
  timeout: 30
  protocols: ["http", "ftp"]
EOF

# Set Python path
echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)" >> ~/.bashrc

echo ""
echo "✅ FAIZ AI Setup Complete!"
echo ""
echo "To use:"
echo "1. source venv/bin/activate"
echo "2. python main.py 'your search query'"
echo ""
echo "Example:"
echo "python smain.py 'linux documentation pdf'"
