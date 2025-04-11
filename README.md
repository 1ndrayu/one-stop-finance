# 💸 one-stop-finance

A cohesive API hub for integrating diverse financial services — including capital, assets, debt, tokens, and payments — under a unified backend infrastructure.

> Built with FastAPI + PostgreSQL, this project is modular, extensible, and aims to simulate a real-world fintech stack with authentication, user management, token operations, and market-level mechanics.

---

## 📦 Current Modules

### ✅ `accounts/`
User authentication and identity layer
- **Register / Login** with JWT-based auth
- **Password hashing** and token security
- Built-in **roles** & scalable user modeling
- Ready for user-wallet linking and permissions

### 🔄 `app/`
Core FastAPI app wiring
- Central `main.py` with modular route inclusion
- Database setup (`database.py`) with SQLAlchemy
- Structured for clean expansion

---

## 🔜 Roadmap

> The project is actively growing. Here's what's coming:

| Module         | Status   | Description |
|----------------|----------|-------------|
| `accounts/`    | ✅ Done   | Auth, login, JWT, roles |
| `wallets/`     | 🔜 Planned | User balances, wallets, transfers |
| `tokens/`      | 🔜 Planned | Tokenize debt/assets/capital |
| `markets/`     | 🔜 Planned | Simulated trading, liquidity |
| `payments/`    | 🔜 Planned | Gateway integrations & transfers |

---

## ⚙️ Tech Stack

- **Python 3.11**
- **FastAPI** (Web framework)
- **SQLAlchemy** + **PostgreSQL** (ORM + DB)
- **JWT Auth** with `python-jose` & `passlib`
- Modular, scalable, production-oriented code structure

---

## 🛠 Setup Instructions

# Clone
git clone https://github.com/1ndrayu/one-stop-finance.git
cd one-stop-finance

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload

# Interactive Swagger UI:
http://localhost:8000/docs

