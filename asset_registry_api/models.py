from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    assets = relationship("Asset", back_populates="owner")


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_type = Column(String, index=True)
    provider_name = Column(String)
    account_number = Column(String)
    balance = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    verified = Column(Boolean, default=False)
    verification_source = Column(String, default="User Input")
    notes = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="assets")

from enum import Enum as PyEnum

class RiskFlagEnum(str, enum.Enum):
    none = "none"
    unverified = "unverified"
    high_value_unverified = "high_value_unverified"
    unknown_type = "unknown_type"

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_type = Column(String, nullable=False)
    provider_name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    verified = Column(Boolean, default=False)
    verification_source = Column(String, default="User Input")
    notes = Column(String, default="")
    
    risk_flag = Column(SqlEnum(RiskFlagEnum), default=RiskFlagEnum.none)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="assets")
