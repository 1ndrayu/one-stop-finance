# 💸 one-stop-finance

A cohesive API hub for integrating diverse financial services — including capital, assets, debt, tokens, and payments — under a unified backend infrastructure.

> Built with FastAPI + PostgreSQL, this project is modular, extensible, and aims to simulate a real-world fintech stack with authentication, user management, token operations, and market-level mechanics.

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

