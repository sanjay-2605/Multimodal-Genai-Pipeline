from fastapi import FastAPI
from backend.routes import rag, image, health

app = FastAPI(title="Multimodal GenAI Pipeline")

app.include_router(rag.router)
app.include_router(image.router)
app.include_router(health.router)
