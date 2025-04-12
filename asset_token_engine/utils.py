import uuid
import random
import string
from typing import Any, Dict

# Function to generate a unique identifier for assets or tokens
def generate_uid(prefix: str = "AST") -> str:
    """Generate a unique identifier with an optional prefix"""
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


# Function to generate a random token for testing or initial validation
def generate_random_token(length: int = 32) -> str:
    """Generate a random token, e.g., for temporary access"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Function to clean up document data, ensuring it's a valid JSON object
def clean_document_data(doc_data: Any) -> Dict:
    """Cleans and ensures the document data is in the correct format"""
    if isinstance(doc_data, dict):
        return doc_data  # Already a valid dictionary
    elif isinstance(doc_data, str):
        try:
            return eval(doc_data)  # Convert stringified dict to actual dict (be cautious!)
        except Exception:
            return {}  # Return empty dict if the data isn't valid
    return {}

# Function to validate asset values (simple checks for demo purposes)
def validate_asset_value(value: float) -> bool:
    """Ensure the asset value is reasonable (positive and within a defined range)"""
    if value <= 0 or value > 10_000_000:  # Set a threshold or limit
        raise ValueError(f"Asset value must be between 0 and 10,000,000, but got {value}")
    return True

# Function to prepare token metadata (e.g., fractionalizing values)
def prepare_token_metadata(asset_value: float, num_tokens: int) -> float:
    """Calculate individual token value by dividing asset value by token count"""
    if num_tokens <= 0:
        raise ValueError("Number of tokens must be greater than zero")
    return round(asset_value / num_tokens, 2)

