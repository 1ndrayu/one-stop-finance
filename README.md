# 💸 one-stop-finance

A cohesive API hub for integrating diverse financial services — including capital, assets, debt, tokens, and payments — under a unified backend infrastructure.

> Built with FastAPI + PostgreSQL, this project is modular, extensible, and aims to simulate a real-world fintech stack with authentication, user management, token operations, and market-level mechanics.

---
# Core Modules
- Asset Tokenization Engine	Convert physical assets into digital tokens	Python / FastAPI
- KYC/AML Module	Verify identity with Aadhaar + PAN	API integrations: Digilocker, Karza
- Issuer Dashboard	Interface to register assets and issue tokens	React / Next.js
- Investor Portal	Buy/sell/view tokens, manage portfolio	React / WalletConnect
- Smart Contract Layer	Represent tokenized assets on-chain	Solidity / Polygon
- Compliance Layer	Handle SEBI sandbox & regulatory reporting	Manual + API logging
- Custody + Escrow	Hold real assets or legal agreements	Partner integration
---

# 🛠 Setup Instructions

## Clone
git clone https://github.com/1ndrayu/one-stop-finance.git
cd one-stop-finance

## Install dependencies
pip install -r requirements.txt

## Run the API
uvicorn app.main:app --reload

## Interactive Swagger UI:
http://localhost:8000/docs
