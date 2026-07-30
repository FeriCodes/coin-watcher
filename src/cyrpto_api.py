import requests
from datetime import datetime


class Crypto:
    def __init__(self, tokens_dict):
        """
        Initializes the Crypto class.
        We pass the tokens dictionary here so the class is self-contained.
        """
        self.tokens = tokens_dict

    @staticmethod
    def get_last_updated() -> str:
        """Returns the current system time in a readable format."""
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def format_price(price: float) -> str:
        """Formats crypto prices with extra precision for coins priced under $1."""
        if price is None:
            return "$0.00"

        if price < 1:
            formatted = f"{price:.8f}".rstrip("0").rstrip(".")
            return f"${formatted}"

        return f"${price:,.2f}"

    def get_prices(self) -> dict:
        """Fetches prices for tokens using their CoinGecko IDs."""

        coin_ids = [
            info["value"] for info in self.tokens.values() if info.get("type") == "id"
        ]

        if not coin_ids:
            return {}

        ids_param = ",".join(coin_ids)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_param}&vs_currencies=usd"

        prices = {}
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for name, info in self.tokens.items():
                    coin_id = info.get("value")
                    if info.get("type") == "id" and coin_id in data:
                        raw_price = data[coin_id]["usd"]

                        prices[name] = self.format_price(raw_price)
        except Exception as e:
            print(f"Error fetching CoinGecko prices: {e}")

        return prices
