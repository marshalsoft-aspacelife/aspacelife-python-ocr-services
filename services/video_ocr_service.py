import cv2
import pytesseract
import os

class VideoToTextExtractorClass:

    SUPPORTED_VIDEO_EXTENSIONS = {".move", ".mp4", ".wav"}
    MAX_IMAGE_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    def __init__(self, frame_interval=30):
        """
        Initializes the VideoTextExtractor.
        """
        self.frame_interval = frame_interval
        print(f"VideoTextExtractor initialized. Will process every {self.frame_interval}th frame.")
    
    @classmethod
    def validate_video_extension(cls, filename: str) -> bool:
            return any(filename.lower().endswith(ext) for ext in cls.SUPPORTED_VIDEO_EXTENSIONS)
    
    @classmethod
    def validate_video_size(cls, file_size: int) -> bool:
        return file_size <= cls.MAX_IMAGE_FILE_SIZE
    
    @classmethod
    def extract_text(self, video_path):
        """
        Extracts text from a video by processing frames using OCR.
        """
        if not os.path.exists(video_path):
            print(f"Error: Video file not found at {video_path}")
            return 

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error: Could not open video file {video_path}")
            return

        frame_count = 0
        extracted_texts = []

        print(f"Starting text extraction from {video_path}...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % self.frame_interval == 0:
                print(f"Processing frame {frame_count}...")
                # Convert frame to grayscale for better OCR performance
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Use Tesseract to do OCR on the frame
                text = pytesseract.image_to_string(gray_frame)
                if text.strip(): # Only add if some text is found
                    extracted_texts.append(f"--- Frame {frame_count} ---\n{text.strip()}\n")

            frame_count += 1

        cap.release()

        print(f"Text extraction complete. Extracted {len(extracted_texts)} text blocks.")
        return extracted_texts

