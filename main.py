from fastapi import FastAPI, File, UploadFile, HTTPException, status

import logging
from api.routes.ocr_image import UploadImage
from api.routes.ocr_video import UploadVideo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize FastAPI app
app = FastAPI(
     title="Aspacelife OCR Text Detection API",
    description="API for extracting text from images",
    version="1.0.0"
)

@app.post("/ocr/image")
async def upload_image(file: UploadFile = File(...)):
    return await UploadImage(file)

@app.post("/ocr/video")
async def upload_video(file: UploadFile = File(...)):
    return await UploadVideo(file)