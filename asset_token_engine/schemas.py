from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from decimal import Decimal

class AssetCreateRequest(BaseModel):
    name: str
    issuer_id: UUID
    asset_type: str
    value: Decimal
    risk_rating: Optional[int] = Field(default=5, ge=1, le=10)
    documents: Optional[dict] = None
    num_tokens: int = Field(gt=0)

class TokenizationResponse(BaseModel):
    asset_id: UUID
    tokens_created: int
