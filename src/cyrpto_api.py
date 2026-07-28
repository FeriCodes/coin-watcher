import requests
from src.tokens import TOKENS


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
                    prices[name] = data[coin_id]["usd"]

    except Exception as e:
        print(f"Error fetching prices: {e}")

    return prices


if __name__ == "__main__":
    result = get_prices()
    print("\n💰 Crypto Prices:")
    for name, price in result.items():
        print(f"  • {name}: ${price:,.5f} USD")
