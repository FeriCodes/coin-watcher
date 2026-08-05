import requests
from datetime import datetime
from src.tokens import TOKENS
import os
from dotenv import load_dotenv

load_dotenv()
CRYPTO_API = os.getenv("CRYPTO_API")


class Crypto:
    def __init__(self, tokens_dict):
        """
        Initializes the Crypto class.
        We pass the tokens dictionary here so the class is self-contained.
        """
        self.tokens = tokens_dict
        self.api_key = CRYPTO_API
        self.headers = {"x-cg-demo-api-key": self.api_key}

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

    def get_prices_with_ids(self) -> dict:
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
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for name, info in self.tokens.items():
                    coin_id = info.get("value")
                    if info.get("type") == "id" and coin_id in data:
                        raw_price = data[coin_id]["usd"]
                        # Fallback to key 'name' if 'name' property is missing
                        display_name = info.get("name", name)
                        prices[display_name] = self.format_price(raw_price)
        except Exception as e:
            print(f"Error fetching CoinGecko prices: {e}")

        return prices

    def get_prices_with_contract(self) -> dict:
        """Fetches prices for tokens using their contract addresses via CoinGecko."""
        prices = {}

        # Dictionary to map our network names to CoinGecko's platform IDs
        network_mapping = {
            "ton": "the-open-network",
            "bsc": "binance-smart-chain",
            "eth": "ethereum",
        }

        for name, info in self.tokens.items():
            if info.get("type") == "contract":
                contract_address = info.get("value")
                net = info.get("network", "eth")
                platform_id = network_mapping.get(net, net)

                url = f"https://api.coingecko.com/api/v3/coins/{platform_id}/contract/{contract_address}"

                try:
                    response = requests.get(url, headers=self.headers, timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        raw_price = data["market_data"]["current_price"]["usd"]

                        display_name = info.get("name", name)
                        prices[display_name] = self.format_price(raw_price)
                except Exception as e:
                    print(f"Error fetching contract price for {name}: {e}")

        return prices

    def get_all_prices(self) -> dict:
        """
        Master method! Fetches prices from CoinGecko (both via IDs and Contracts)
        and combines them into a single dictionary.
        """
        all_prices = {}

        cg_prices = self.get_prices_with_ids()
        all_prices.update(cg_prices)

        contract_prices = self.get_prices_with_contract()
        all_prices.update(contract_prices)

        return all_prices


# این بلوک فقط زمانی اجرا می‌شه که مستقیم همین فایل رو ران کنی
if __name__ == "__main__":
    crypto_app = Crypto(TOKENS)

    print("Fetching all prices...")
    final_prices = crypto_app.get_all_prices()

    print(final_prices)
