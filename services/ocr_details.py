# ============================================================================
# OCR Detailed Response Class
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional, List

class OCRDetailedResponse(BaseModel):
    """Detailed response with word-level information"""
    success: bool
    text: str
    words: List[dict] = Field(..., description="Word-level OCR data")
    language: str
    processing_time: float
    timestamp: str
