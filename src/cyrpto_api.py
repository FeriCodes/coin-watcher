import requests
from tokens import TOKENS


def get_prices():
    prices = {}

    for name, info in TOKENS.items():
        if info["type"] == "id":
            coin_id = info["value"]
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if coin_id in data:
                        prices[name] = data[coin_id]["usd"]
            except Exception as e:
                print(f"Error fetching {name}: {e}")

    return prices


if __name__ == "__main__":
    result = get_prices()
    print("\n💰 Crypto Prices:")
    for name, price in result.items():
        print(f"  • {name}: ${price:,.2f} USD")
