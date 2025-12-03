
# ============================================================================
# OCR Service Class
# ============================================================================

import pytesseract
from PIL import Image

class OCRService:
    SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}
    SUPPORTED_VIDEO_EXTENSIONS = {".move", ".mp4", ".wav"}
    MAX_IMAGE_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    
    def __init__(self, tesseract_cmd=None):
        """
        Initialize the ImageTextExtractor.
        Optionally set the path to the tesseract executable.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    @classmethod
    def validate_extension_image(cls, filename: str) -> bool:
        return any(filename.lower().endswith(ext) for ext in cls.SUPPORTED_IMAGE_EXTENSIONS)

    @classmethod
    def validate_extension_video(cls, filename: str) -> bool:
            return any(filename.lower().endswith(ext) for ext in cls.SUPPORTED_VIDEO_EXTENSIONS)

    @classmethod
    def validate_image_size(cls, file_size: int) -> bool:
        return file_size <= cls.MAX_IMAGE_FILE_SIZE
    
    @classmethod
    def validate_video_size(cls, file_size: int) -> bool:
        return file_size <= cls.MAX_IMAGE_FILE_SIZE
    
    @classmethod
    async def extract_text(self, image_path):
        """
        Extract text from an image file.
        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        try:
          # Open the image using Pillow
            img_for_ocr = Image.open(image_path)

            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(img_for_ocr)
            # remove file from server
            return text.strip()
        except Exception as e:
            return f"Error extracting text: {str(e)}"
    



    

   