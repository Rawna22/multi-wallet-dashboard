import os, json, requests
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPCS = {
    "Ethereum": os.getenv("ETHEREUM_RPC"),
    "Base": os.getenv("BASE_RPC"),
    "zkSync": os.getenv("ZKSYNC_RPC"),
    "Optimism": os.getenv("OPTIMISM_RPC"),
}

COVALENT_API_KEY = os.getenv("COVALENT_API_KEY")

# Load list wallet
with open("wallets.json") as f:
    WALLETS = json.load(f)

def get_native_balance(wallet, rpc_url):
    if not rpc_url:
        return None
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    balance_wei = w3.eth.get_balance(wallet)
    return float(w3.from_wei(balance_wei, "ether"))

def get_chain_balances(chain, rpc_url, wallet_list):
    balances = []
    for wallet in wallet_list:
        try:
            bal = get_native_balance(wallet, rpc_url)
            balances.append({"Wallet": wallet, "Balance": bal})
        except Exception:
            balances.append({"Wallet": wallet, "Balance": 0})
    return balances

def get_token_balances(wallet):
    url = f"https://api.covalenthq.com/v1/1/address/{wallet}/balances_v2/"
    res = requests.get(url, params={"key": COVALENT_API_KEY})
    if res.status_code == 200:
        return res.json()["data"]["items"]
    return []
