from services.video_ocr_service import VideoToTextExtractorClass
from utils.api_response import ApiResponse
from fastapi import File, UploadFile, HTTPException
from utils.save_file import save_upload_file
from pathlib import Path

async def UploadVideo(
        postId:str,
        resourceId:str,
        videoData: UploadFile = File(...)
        ):
    if not VideoToTextExtractorClass.validate_video_extension(videoData.filename):
        return ApiResponse(False,"Unsupported video file extension",{})
    saved_file = await save_upload_file(videoData,"video")
    print("Saved file info:", saved_file)
    # Return the success message and the full,file permanent file path
    response = await VideoToTextExtractorClass.extract_text(saved_file.filepath)
    return ApiResponse(True,"Valid file",{
            "message": f"File '{saved_file.filename}' uploaded successfully!",
            "filename": saved_file.filename,
            "saved_path_absolute": str(saved_file.filepath),
            "content_type": videoData.content_type,
            "file_size": saved_file.filesize,
            "text":response
        })