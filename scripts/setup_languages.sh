#!/bin/bash

echo "Installing additional Tesseract language packs..."

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux - Install common languages
    sudo apt-get install -y \
        tesseract-ocr-fra \
        tesseract-ocr-spa \
        tesseract-ocr-deu \
        tesseract-ocr-ita \
        tesseract-ocr-por \
        tesseract-ocr-rus \
        tesseract-ocr-ara \
        tesseract-ocr-chi-sim \
        tesseract-ocr-jpn
    echo "Language packs installed on Linux"
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install tesseract-lang
    echo "Language packs installed on macOS"
    
else
    echo "Unsupported OS."
fi

# List installed languages
tesseract --list-langs