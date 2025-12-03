# ============================================================================
# Pydantic Models for Request/Response
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional, List

class OCRResponse(BaseModel):
    """Response model for OCR results"""
    success: bool = Field(..., description="Whether OCR was successful")
    text: str = Field(..., description="Extracted text from image")
    confidence: Optional[float] = Field(None, description="Overall confidence score (0-100)")
    language: str = Field(..., description="Language used for OCR")
    processing_time: float = Field(..., description="Processing time in seconds")
    timestamp: str = Field(..., description="Timestamp of processing")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "text": "Hello World",
                "confidence": 95.5,
                "language": "eng",
                "processing_time": 0.523,
                "timestamp": "2024-11-25T10:30:00"
            }
        }
