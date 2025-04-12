from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from . import models, schemas, service
from app.database import get_db  # adjust path if needed

router = APIRouter(prefix="/assets", tags=["Asset Tokenization"])

@router.post("/tokenize", response_model=schemas.TokenizationResponse)
def tokenize_asset(request: schemas.AssetCreateRequest, db: Session = Depends(get_db)):
    try:
        return service.tokenize_asset(db, request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
