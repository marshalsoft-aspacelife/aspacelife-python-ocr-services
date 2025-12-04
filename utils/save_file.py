from fastapi import UploadFile
import os
import uuid
import io
from PIL import Image
from dotenv import load_dotenv
from utils.save_image_file_response import SaveImageFileResponseClass
load_dotenv()

async def save_upload_file(file: UploadFile) -> SaveImageFileResponseClass:
   # Get file extension
        contents = await file.read()
        base_dir = os.path.abspath(__file__)

        file_ext = os.path.splitext(file.filename)[1].lower()
        unique_filename = f"{uuid.uuid4()}{file_ext}"
      
        output_path = os.path.join(os.environ.get("UPLOAD_DIR"), unique_filename)
        
        # Check if file already exists
            # Add timestamp to make it unique
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # file_path = os.path.join(base_dir, file_path)
        
        # Save file
        image_stream = io.BytesIO(contents)

        # Open the image using Pillow
        img = Image.open(image_stream)
        # Save the image. You can specify format if needed, e.g., img.save(output_path, format="PNG")
        img.save(output_path)
        return SaveImageFileResponseClass(unique_filename, output_path,file.size)
