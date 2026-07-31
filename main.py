from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.crypto_api import Crypto
from src.tokens import TOKENS

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


@app.get("/health")
def health_check():
    return {"status": "healthy"}
