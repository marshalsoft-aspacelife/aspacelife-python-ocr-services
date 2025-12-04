# OCR in Python
Aspacelife Text Detection Service (OCR) Python Project
## Overview
An Aspacelife Python project for Optical Character Recognition (OCR) to extract text from images and video.

## Author's Details
- Name: Marshall Ekene
- Email: [ekene.marshall@aspacelifetech.com](mail:ekene.marshall@aspacelifetech.com)
- Github: [marshallekene@marshalsoft-aspacelife](https://github.com/marshalsoft-aspacelife/aspacelife-python-ocr-services)

## Features
- Extract text from image and video files
- Support for multiple image formats (png,jpg,jpeg,tiff,bmp,gif)

## Requirements
```
fastapi
uvicorn
python-multipart
pillow
pytesseract
pydantic
pydantic-settings
python-dotenv
aiofiles
quixstreams
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
# RUN api
uvicorn main:app --reload
```

## Project Structure
```
OCR/
├── readMe.md
├── main.py
├── requirements.txt
└── api/routes
└── models/
└── scripts/
└── services/
└── test_images/
└── test_videos/
└── utils/
└── .env.example
└── .env
└── .gitignore
```

## License
MIT
