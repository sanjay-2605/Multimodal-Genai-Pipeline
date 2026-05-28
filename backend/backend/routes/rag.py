from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.rag_service import query_rag

router = APIRouter(prefix="/rag", tags=["RAG"])

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
def rag_query(request: QueryRequest):
    response = query_rag(request.query)
    return {"response": response}
  
