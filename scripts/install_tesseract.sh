#!/bin/bash

echo "Installing Tesseract OCR..."

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr
    sudo apt-get install -y tesseract-ocr-eng
    echo "Tesseract installed on Linux"
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install tesseract
    echo "Tesseract installed on macOS"
    
else
    echo "Unsupported OS. Please install Tesseract manually."
    echo "Visit: https://github.com/tesseract-ocr/tesseract"
fi

# Verify installation
tesseract --version