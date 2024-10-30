import requests
import pandas as pd
from datetime import datetime

def fetch_memecoins():
    """Fetches memecoin market data from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "category": "memes",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Failed to fetch data.")
        return None
    return response.json()

def analyze_memecoins(data):
    """Analyzes memecoin data to find potentially trustworthy coins."""
    min_volume = 500000
    min_market_cap = 5000000

    print(f"\nMemecoin Analysis ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):")
    print("Filtering for coins with high volume and market cap.")

    df = pd.DataFrame(data)
    filtered_df = df[
        (df['total_volume'] > min_volume) &
        (df['market_cap'] > min_market_cap) &
        (df['price_change_percentage_24h'] > 0)
    ]

    columns = ["id", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
    result_df = filtered_df[columns].sort_values(by="price_change_percentage_24h", ascending=False)

    if not result_df.empty:
        print("Top Trending Memecoins (Filtered):")
        print(result_df.head(10))
    else:
        print("No memecoins meet the criteria.")

def main():
    memecoins_data = fetch_memecoins()
    if memecoins_data:
        analyze_memecoins(memecoins_data)
    else:
        print("No data available for memecoins.")

import requests
import pandas as pd
from datetime import datetime

def fetch_memecoins():
    """Fetches memecoin market data from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "category": "memes",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Failed to fetch data.")
        return None
    return response.json()

def analyze_memecoins(data):
    """Analyzes memecoin data to find potentially trustworthy coins."""
    min_volume = 500000
    min_market_cap = 5000000

    print(f"\nMemecoin Analysis ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):")
    print("Filtering for coins with high volume and market cap.")

    df = pd.DataFrame(data)
    filtered_df = df[
        (df['total_volume'] > min_volume) &
        (df['market_cap'] > min_market_cap) &
        (df['price_change_percentage_24h'] > 0)
    ]

    columns = ["id", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
    result_df = filtered_df[columns].sort_values(by="price_change_percentage_24h", ascending=False)

    if not result_df.empty:
        print("Top Trending Memecoins (Filtered):")
        print(result_df.head(10))
    else:
        print("No memecoins meet the criteria.")

def main():
    memecoins_data = fetch_memecoins()
    if memecoins_data:
        analyze_memecoins(memecoins_data)
    else:
        print("No data available for memecoins.")

if __name__ == "__main__":
    main()if __name__ == "__main__":
    main()

