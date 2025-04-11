from fastapi import FastAPI
from app.accounts import routes as accounts_routes

app = FastAPI()
app.include_router(accounts_routes.router)
