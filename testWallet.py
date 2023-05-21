import requests

def check_wallet_provider(address):
    # Check if the address is associated with MetaMask
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        txs = data["result"]
        for tx in txs:
            # Check if the transaction data is associated with MetaMask
            if tx["to"] == "0x888888888889c00c67689029d7856aac1065ec11":
                return "MetaMask"
            # Check if the transaction data is associated with Coinbase
            elif tx["to"] == "0x21a31e7ee8af9d0d99d676c04f994f93923f9c9e":
                return "Coinbase"
            # Check if the transaction data is associated with WazirX
            elif tx["to"] == "0x11e2278d3d8f5bfffcf5a7bc5e395c8441dbfa5c" and tx["input"].startswith("0x23b872dd"):
                return "WazirX"
            # Check if the transaction data is associated with CoinDCX
            elif tx["to"] == "0x6a03d2b2441c5ec59ca5a9f78bafbe10c03d8d4b" and tx["input"].startswith("0xf305d719"):
                return "CoinDCX"
        # If the address is not associated with any of the wallets
        return "Unknown"
    else:
        return "Error"

# Example usage
address = "0x6a03d2b2441c5ec59ca5a9f78bafbe10c03d8d4b"

wallet = check_wallet_provider(address)
print(f"Address is associated with {wallet}")
