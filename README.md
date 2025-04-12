# One-Stop-Finance

A simple platform to tokenize real-world assets and manage them through a backend, issuer dashboard, and investor portal.

---

## Quick Setup (Windows)

---

### 1. Clone the Repository

```powershell
git clone https://github.com/YOUR_USERNAME/one-stop-finance.git
cd one-stop-finance
```

---

### 2. Backend Setup (FastAPI)

```powershell
cd asset_token_engine
copy .env.example .env
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: `http://localhost:8000/docs`

---

### 3. PostgreSQL Setup

Create a database named `asset_token_engine` using pgAdmin or CLI.

---

### 4. Issuer Dashboard (React / Next.js)

```powershell
cd ..\issuer-dashboard
copy .env.local.example .env.local
npm install
npm run dev
```

Visit: `http://localhost:3000`

---

### 5. Investor Portal (React / WalletConnect)

```powershell
cd ..\investor-portal
copy .env.local.example .env.local
npm install
npm run dev
```

Visit: `http://localhost:3001`

---

## Environment Files

Each folder has a `.env.example` or `.env.local.example`.

- Copy it to `.env` or `.env.local`
- Fill in your own values
- Do **not** commit `.env` files

---

## You're Ready

- Backend runs at `localhost:8000`
- Issuer dashboard at `localhost:3000`
- Investor portal at `localhost:3001`

---
