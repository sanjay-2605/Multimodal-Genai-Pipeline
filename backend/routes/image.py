from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/image", tags=["Image"])

class ImageRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_image(request: ImageRequest):

    return {
        "message": "Image generation pipeline triggered",
        "prompt": request.prompt
    }
