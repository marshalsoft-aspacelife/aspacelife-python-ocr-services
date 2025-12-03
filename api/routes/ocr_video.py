from services.ocr_service import OCRService
from utils.api_response import ApiResponse
from fastapi import File, UploadFile, HTTPException
import aiofiles
import os
import uuid
from pathlib import Path
UPLOAD_FOLDER = Path("test_videos")

async def UploadVideo(file: UploadFile = File(...)):
    if not OCRService.validate_extension_video(file.filename):
        return ApiResponse(False,"Unsupported file extension",{})
    
    contents = await file.read()
    if not OCRService.validate_video_size(len(contents)):
        raise HTTPException(status_code=400, detail=ApiResponse(False,"File size exceeds limit",{}))
    
    original_filename = file.filename
    file_extension = os.path.splitext(original_filename)[1]

    # 2. Generate a secure, unique filename to prevent overwrites and path traversal attacks
    unique_filename = f"{uuid.uuid4()}{file_extension}"
        
    # 3. Define the full path where the file will be saved
    # The Path object handles joining directory names correctly for all operating systems
    saved_file_path: Path = UPLOAD_FOLDER / unique_filename
    async with aiofiles.open(saved_file_path, 'wb') as out_file:
        # Read chunks from the UploadFile stream and write them to the disk file
        while content := await file.read(1024 * 1024):  # Read in 1MB chunks
            await out_file.write(content)

    # 5. Get the absolute path of the saved file
    absolute_path = saved_file_path.resolve()
        
    # Return the success message and the full, permanent file path
    response = await OCRService.extract_text(absolute_path)
     
    return ApiResponse(True,"Valid file",{
            "message": f"File '{original_filename}' uploaded successfully!",
            "filename": unique_filename,
            "saved_path_relative": str(saved_file_path),
            "saved_path_absolute": str(absolute_path),
            "content_type": file.content_type,
            "text":response
        })
