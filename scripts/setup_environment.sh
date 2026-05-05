#!/bin/bash
set -e

echo "Setting up environment for Drift Detection dissertation..."

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .

echo "✅ Environment setup complete!"
echo "To activate: source venv/bin/activate"