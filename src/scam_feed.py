import requests
import json
from dotenv import load_dotenv

load_dotenv()

GOPLUS_URL = "https://api.gopluslabs.io/api/v1/address_security"

def check_wallet_reputation(address):
    print(f"\n🔍 Checking reputation for: {address}")
    
    params = {"chain_id": "1"}
    url = f"{GOPLUS_URL}/{address}"
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        result = data.get("result", {})
        
        flags = []
        if result.get("is_blacklist_doubt") == "1": flags.append("Blacklisted")
        if result.get("is_phishing_activities") == "1": flags.append("Phishing")
        if result.get("is_contract_address") == "1": flags.append("Contract")
        if result.get("is_mixer") == "1": flags.append("Mixer/Tumbler")
        if result.get("is_malicious_mining_activities") == "1": flags.append("Malicious Mining")
        if result.get("is_darkweb_transactions") == "1": flags.append("Dark Web Activity")
        if result.get("is_stealing_attack") == "1": flags.append("Stealing Attack")
        
        if flags:
            print(f"🚨 FLAGGED — {', '.join(flags)}")
        else:
            print(f"✅ Clean — no threats detected")
            
        return flags
    else:
        print(f"❌ API Error: {response.status_code}")
        return []

if __name__ == "__main__":
    scam_wallet = "0xd882cfc20f52f2599d84b8e8d58c7fb62cfe344b"
    clean_wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    
    check_wallet_reputation(scam_wallet)
    check_wallet_reputation(clean_wallet)