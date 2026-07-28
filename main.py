from fastapi import FastAPI
from src.cyrpto_api import get_prices

app = FastAPI(title="Crypto Price API", version="1.0")


@app.get("/")
def prices():
    return get_prices()


@app.get("/health")
def health_check():
    return {"status": "healthy"}
