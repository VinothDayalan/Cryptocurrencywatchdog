import requests

def get_wallet_info(address, currency):
    url = f"https://api.blockchair.com/eth/dashboards/address/0x0d8775f648430679a709e98d2b0cb6250d2887ef"
    response = requests.get(url)
    print(response)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return
    data = response.json()
    
    if 'data' not in data or 'address' not in data['data']:
        print(f"Error: wallet info not found")
        return
    balance = data['data']['address'].get('balance')
    transactions = data['data']['address'].get('transaction_count')
    print(f"Address: {address}")
    print(f"Currency: {currency.upper()}")
    print(f"Balance: {balance}")
    print(f"Transaction count: {transactions}")

# Example usage
get_wallet_info("0x0d8775f648430679a709e98d2b0cb6250d2887ef", "eth")
