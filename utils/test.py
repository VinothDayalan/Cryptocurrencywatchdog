import requests

addr = input("Enter an address: ")
url = f"https://blockchain.info/rawaddr/{addr}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Address: {data['address']}")
    print(f"Balance: {data['final_balance'] / 1e8} BTC")
    print(f"Total Received: {data['total_received'] / 1e8} BTC")
    print(f"Total Sent: {data['total_sent'] / 1e8} BTC")
    print(f"Final Balance: {data['final_balance'] / 1e8} BTC")
    # process the data as needed
else:
    print("Request failed")
