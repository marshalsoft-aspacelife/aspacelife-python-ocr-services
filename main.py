from fastapi import FastAPI, File, UploadFile
import uvicorn
import logging
from api.routes.ocr_image import UploadImage
from api.routes.ocr_video import UploadVideo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initApp():
    # Initialize FastAPI app
    app = FastAPI(
        title="Aspacelife OCR Text Detection API",
        description="API for extracting text from images",
        version="1.0.0"
    )

    @app.post("/v1/abaa_image_ocr_processing")
    async def upload_image(
        postId:str,
        resourceId:str,
        imageData: UploadFile = File(...)):
        return await UploadImage(
            postId,
            resourceId,
            imageData
            )

    @app.post("/v1/abaa_video_ocr_processing")
    async def upload_video(
        postId:str,
        resourceId:str,
        videoData: UploadFile = File(...)
        ):
        return await UploadVideo(
            postId,
            resourceId,
            videoData
            )
    
    return app

app = initApp()

if( __name__ == "__main__"):
    uvicorn.run(app, host="localhost", port=3001, log_level="debug", reload=False)
        