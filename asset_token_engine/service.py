from .models import Asset, Token
from sqlalchemy.orm import Session
import uuid

def tokenize_asset(db: Session, asset_data: dict, num_tokens: int):
    asset_id = str(uuid.uuid4())
    asset = Asset(id=asset_id, **asset_data)
    db.add(asset)

    token_value = asset_data['value'] / num_tokens
    tokens = [
        Token(
            id=str(uuid.uuid4()),
            asset_id=asset_id,
            token_number=i+1,
            value=token_value,
            rights="ownership"
        )
        for i in range(num_tokens)
    ]
    db.add_all(tokens)
    db.commit()
    return {"asset_id": asset_id, "tokens_created": num_tokens}
