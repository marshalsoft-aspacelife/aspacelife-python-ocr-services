
# ============================================================================
# OCR Service Class
# ============================================================================

import pytesseract
from PIL import Image
from services.kafka.index import QuixstreamsMessageSender
import sys
import os
import time
from dotenv import load_dotenv
import json
load_dotenv()
import tracemalloc
class ImageToTextServiceClass:
    SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}
    MAX_IMAGE_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    
    def __init__(self, tesseract_cmd=None):
        """
        Initialize the ImageTextExtractor.
        Optionally set the path to the tesseract executable.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    @classmethod
    def validate_image_extension(cls, filename: str) -> bool:
        return any(filename.lower().endswith(ext) for ext in cls.SUPPORTED_IMAGE_EXTENSIONS)


    @classmethod
    def validate_image_size(cls, file_size: int) -> bool:
        return file_size <= cls.MAX_IMAGE_FILE_SIZE
    
    @classmethod
    async def extract_text(self, image_path):
        """
        Extract text from an image file.
        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        try:
            if sys.version_info >= (3, 4):
                tracemalloc.start()
            # Open the image using Pillow
            img_for_ocr = Image.open(image_path)

            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(img_for_ocr)
            # sender = QuixstreamsMessageSender(topic_name="my-output-topic")
            # msg = json.dumps({ "data": text, "timestamp": time.time()})
            # sender.send_message(msg, key=os.environ.get("KAFKA_MESSAGE_KEY","ocr_key"))
            
            tracemalloc.stop()
            # delete image from disk after processing
            os.remove(image_path)
            
            return text.strip()
        except Exception as e:
            return f"Error extracting text: {str(e)}"
    


    

   