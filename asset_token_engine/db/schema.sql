-- assets table
CREATE TABLE assets (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    issuer_id UUID NOT NULL,
    asset_type TEXT CHECK (asset_type IN ('real_estate', 'equity', 'debt', 'other')) NOT NULL,
    value NUMERIC(20, 2) NOT NULL,
    risk_rating INTEGER CHECK (risk_rating >= 1 AND risk_rating <= 10),
    documents JSONB,
    status TEXT CHECK (status IN ('draft', 'tokenized', 'listed', 'archived')) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- tokens table
CREATE TABLE tokens (
    id UUID PRIMARY KEY,
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    owner_id UUID,
    token_number INTEGER NOT NULL,
    value NUMERIC(20, 2) NOT NULL,
    rights TEXT DEFAULT 'ownership',
    status TEXT CHECK (status IN ('active', 'locked', 'transferred', 'burned')) DEFAULT 'active'
);
