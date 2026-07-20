import os
import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("CRYPTO_API_KEY")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]

        print(f"💰 Bitcoin Price: ${bitcoin_price:,} USD")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
