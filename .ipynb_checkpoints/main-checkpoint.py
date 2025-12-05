from fastapi import FastAPI, File, UploadFile, HTTPException, status
from typing import List
from services.image_ocr_service import ImageToTextServiceClass
from utils.api_response import ApiResponse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
     title="Aspacelife OCR Text Detection API",
    description="API for extracting text from images",
    version="1.0.0"
)

@app.post("/ocr/")
async def upload_image(file: UploadFile = File(...)):
    if not ImageToTextServiceClass.validate_extension(file.filename):
        return ApiResponse(False,"Unsupported file extension",{})
    
    contents = await file.read()
    if not ImageToTextServiceClass.validate_size(len(contents)):
        raise HTTPException(status_code=400, detail=ApiResponse(False,"File size exceeds limit",{}))
    
    response = ImageToTextServiceClass.extract_text(file)

    return ApiResponse(True,"Valid file",{"filename": file.filename, "size": len(contents),"text":response})
