from services.ocr_service import OCRService
from utils.api_response import ApiResponse
from fastapi import File, UploadFile, HTTPException
from utils.save_file import save_upload_file
from pathlib import Path

async def UploadImage(file: UploadFile):
    
    if not OCRService.validate_extension_image(file.filename):
        return ApiResponse(False,"Unsupported image file extension",{})
    saved_file = await save_upload_file(file)
    print("Saved file info:", saved_file)
    # Return the success message and the full,file permanent file path
    response = await OCRService.extract_text(saved_file.filepath)
    return ApiResponse(True,"Valid file",{
            "message": f"File '{saved_file.filename}' uploaded successfully!",
            "filename": saved_file.filename,
            "saved_path_absolute": str(saved_file.filepath),
            "content_type": file.content_type,
            "file_size": saved_file.filesize,
            "text":response
        })
