# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user
@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Get user with their assets
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "assets": user.assets
    }

# Add asset for a specific user
from constants import VALID_ASSET_TYPES

@app.post("/users/{user_id}/assets/")
def add_asset_for_user(
    user_id: int,
    asset_type: str,
    provider_name: str,
    account_number: str,
    balance: float,
    verified: bool = False,
    verification_source: str = "User Input",
    notes: str = "",
    db: Session = Depends(get_db)
):
    if asset_type not in VALID_ASSET_TYPES:
        raise HTTPException(status_code=400, detail="Invalid asset type")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    asset = models.Asset(
        asset_type=asset_type,
        provider_name=provider_name,
        account_number=account_number,
        balance=balance,
        verified=verified,
        verification_source=verification_source,
        notes=notes,
        owner=user
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

# Create asset for user
from constants import VALID_ASSET_TYPES
from models import RiskFlagEnum

@app.post("/users/{user_id}/assets/")
def add_asset_for_user(
    user_id: int,
    asset_type: str,
    provider_name: str,
    account_number: str,
    balance: float,
    verified: bool = False,
    verification_source: str = "User Input",
    notes: str = "",
    db: Session = Depends(get_db)
):
    if asset_type not in VALID_ASSET_TYPES:
        raise HTTPException(status_code=400, detail="Invalid asset type")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # --- Risk Flag Logic ---
    risk_flag = RiskFlagEnum.none
    if not verified:
        risk_flag = RiskFlagEnum.unverified
    if not verified and balance > 5000000:
        risk_flag = RiskFlagEnum.high_value_unverified
    if asset_type not in VALID_ASSET_TYPES:
        risk_flag = RiskFlagEnum.unknown_type

    # --- Create Asset with Risk Flag ---
    asset = models.Asset(
        asset_type=asset_type,
        provider_name=provider_name,
        account_number=account_number,
        balance=balance,
        verified=verified,
        verification_source=verification_source,
        notes=notes,
        risk_flag=risk_flag,
        owner=user
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset


from pydantic import BaseModel

class AssetUpdateRequest(BaseModel):
    provider_name: str | None = None
    notes: str | None = None

@app.put("/assets/{asset_id}")
def update_asset(asset_id: int, update_data: AssetUpdateRequest, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    if asset.verified:
        raise HTTPException(status_code=403, detail="Verified assets cannot be modified")

    if update_data.provider_name:
        asset.provider_name = update_data.provider_name
    if update_data.notes:
        asset.notes = update_data.notes

    db.commit()
    db.refresh(asset)
    return asset

@app.delete("/assets/{asset_id}")
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    if asset.verified:
        raise HTTPException(status_code=403, detail="Verified assets cannot be deleted")

    db.delete(asset)
    db.commit()
    return {"detail": "Asset deleted successfully"}

