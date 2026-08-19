import sqlite3
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.coin_watcher import Crypto


def load_tokens():
    conn = sqlite3.connect("tokens.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT symbol, name, coin_type, value, network FROM favorites")
    rows = cursor.fetchall()

    tokens = {}
    for row in rows:
        symbol = row["symbol"]
        tokens[symbol] = {
            "name": row["name"],
            "type": row["coin_type"],
            "value": row["value"],
        }
        if row["network"]:
            tokens[symbol]["network"] = row["network"]
    conn.close()
    return tokens


TOKENS = load_tokens()


app = FastAPI(title="Coin Watcher", version="1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def prices(request: Request):
    crypto_app = Crypto(TOKENS)
    prices_data = crypto_app.get_all_prices()
    time = crypto_app.get_last_updated()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "prices": prices_data, "time": time},
    )


@app.get("/api/prices")
def get_live_prices():
    crypto_app = Crypto(TOKENS)
    prices_data = crypto_app.get_all_prices()
    time = crypto_app.get_last_updated()

    return {"status": "success", "prices": prices_data, "time": time}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
