import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")
BASE_URL = "https://api.etherscan.io/v2/api"

def get_wallet_transactions(address):
    print(f"\n🔍 Fetching transactions for: {address}")
    params = {
    "chainid": 1,
    "module": "account",
    "action": "txlist",
    "address": address,
    "startblock": 0,
    "endblock": 99999999,
    "page": 1,
    "offset": 10,
    "sort": "desc",
    "apikey": API_KEY
}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["status"] == "1":
        print(f"✅ Found {len(data['result'])} transactions")
        return data["result"]
    else:
        print(f"❌ Error: {data['message']}")
        return []

def display_transactions(transactions):
    for tx in transactions:
        value_eth = int(tx["value"]) / 1e18
        print(f"  → {tx['hash'][:20]}...  |  {value_eth:.4f} ETH  |  {tx['from'][:10]}...")

if __name__ == "__main__":
    # Vitalik Buterin's wallet — famous public address, good for testing
    test_wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    txs = get_wallet_transactions(test_wallet)
    display_transactions(txs)