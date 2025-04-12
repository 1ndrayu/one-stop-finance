from sqlalchemy import Column, String, Integer, Numeric, Enum, ForeignKey, Text, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database import Base  # Adjust this import if you use a different base setup

ASSET_TYPES = ('real_estate', 'equity', 'debt', 'other')
ASSET_STATUSES = ('draft', 'tokenized', 'listed', 'archived')
TOKEN_STATUSES = ('active', 'locked', 'transferred', 'burned')

class Asset(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    issuer_id = Column(UUID(as_uuid=True), nullable=False)
    asset_type = Column(Enum(*ASSET_TYPES, name="asset_type_enum"), nullable=False)
    value = Column(Numeric(20, 2), nullable=False)
    risk_rating = Column(Integer)
    documents = Column(JSONB, nullable=True)
    status = Column(Enum(*ASSET_STATUSES, name="asset_status_enum"), default='draft')
    created_at = Column(DateTime, default=datetime.utcnow)

    tokens = relationship("Token", back_populates="asset", cascade="all, delete-orphan")

class Token(Base):
    __tablename__ = "tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    asset_id = Column(UUID(as_uuid=True), ForeignKey("assets.id", ondelete="CASCADE"))
    owner_id = Column(UUID(as_uuid=True), nullable=True)
    token_number = Column(Integer, nullable=False)
    value = Column(Numeric(20, 2), nullable=False)
    rights = Column(Text, default="ownership")
    status = Column(Enum(*TOKEN_STATUSES, name="token_status_enum"), default='active')

    asset = relationship("Asset", back_populates="tokens")
