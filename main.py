from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.cyrpto_api import get_prices
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Crypto Price API", version="1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def prices(request: Request):
    prices_data = get_prices()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "prices": prices_data},
    )


@app.get("/health")
def health_check():
    return {"status": "healthy"}
