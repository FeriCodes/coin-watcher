import requests
from src.tokens import TOKENS


def format_crypto_price(price: float) -> str:
    """Formats crypto prices with extra precision for coins priced under $1."""

    if price is None:
        return "$0.00"

    if price < 1:
        formatted = f"{price:.8f}".rstrip("0").rstrip(".")
        return f"${formatted}"

    return f"${price:,.2f}"


def get_prices():
    coin_ids = [info["value"] for info in TOKENS.values() if info.get("type") == "id"]

    if not coin_ids:
        return {}

    ids_param = ",".join(coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_param}&vs_currencies=usd"

    prices = {}
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for name, info in TOKENS.items():
                coin_id = info.get("value")
                if coin_id in data:
                    raw_price = data[coin_id]["usd"]

                    prices[name] = format_crypto_price(raw_price)
    except Exception as e:
        print(f"Error fetching prices: {e}")

    return prices
