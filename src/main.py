from ingest import get_wallet_transactions, display_transactions
from scam_feed import check_wallet_reputation
import json
import os
from datetime import datetime

def analyze_wallet(address):
    print(f"\n{'='*60}")
    print(f"  CryptoShield AI — Wallet Analysis")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    # Check reputation
    flags = check_wallet_reputation(address)
    
    # Get transactions
    txs = get_wallet_transactions(address)
    display_transactions(txs)
    
    # Risk summary
    print(f"\n📊 Risk Summary for {address[:10]}...")
    print(f"   Threat flags : {flags if flags else 'None'}")
    print(f"   Transactions : {len(txs)} recent")
    print(f"   Risk level   : {'🔴 HIGH' if flags else '🟢 LOW'}")
    
    # Save to file
    os.makedirs("../data", exist_ok=True)
    report = {
        "timestamp": datetime.now().isoformat(),
        "address": address,
        "flags": flags,
        "transaction_count": len(txs),
        "risk_level": "HIGH" if flags else "LOW"
    }
    filename = f"../data/report_{address[:8]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    print(f"💾 Report saved: {filename}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    test_wallets = [
        "0xd882cfc20f52f2599d84b8e8d58c7fb62cfe344b",
        "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    ]
    for wallet in test_wallets:
        analyze_wallet(wallet)