import requests
import json
import re


def is_valid_eth_address(address):
    if not re.match(r'^(0x)?[0-9a-fA-F]{40}$', address):
        return False
    return True

address = input("Enter an Ethereum address: ")
if not is_valid_eth_address(address):
    print("Invalid Ethereum address")
else:
    api_key = "A37RMWJCF8HX5BF378QJDZGAMXRVFYHABJ"
    balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    tx_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={api_key}"
    balance_response = requests.get(balance_url)
    tx_response = requests.get(tx_url)

    if balance_response.status_code == 200 and tx_response.status_code == 200:
        balance_data = json.loads(balance_response.text)
        tx_data = json.loads(tx_response.text)
        balance_in_wei = int(balance_data["result"])
        balance_in_eth = balance_in_wei / 1e18
        total_received_in_wei = sum([int(tx["value"]) for tx in tx_data["result"] if tx["to"].lower() == address.lower()])
        total_received_in_eth = total_received_in_wei / 1e18
        total_sent_in_wei = sum([int(tx["value"]) for tx in tx_data["result"] if tx["from"].lower() == address.lower()])
        total_sent_in_eth = total_sent_in_wei / 1e18
        num_transactions = len(tx_data["result"])
        print(f"Address: {address}")
        print(f"Balance: {balance_in_eth} ETH")
        print(f"Total Received: {total_received_in_eth} ETH")
        print(f"Total Sent: {total_sent_in_eth} ETH")
        print(f"Number of Transactions: {num_transactions}")
    else:
        print("Request failed")
