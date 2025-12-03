# ============================================================================
# OCR Error Response Class
# 

class ErrorResponse(BaseModel):
    """Error response model"""
    success: bool = False
    error: str = Field(..., description="Error message")
    timestamp: str
