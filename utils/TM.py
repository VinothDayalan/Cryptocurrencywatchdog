import requests

API_ENDPOINT = "https://api.blockchain.info/rawaddr/"
address = "1LGgfryxMwUUCEHkRuey86fCa66g1aUogr"
method = "address/" + address + "?format=json"
print("Requesting", API_ENDPOINT + method)
response = requests.get(API_ENDPOINT + method)


if response.status_code == 200:
    try:
        data = response.json()
        for transaction in data["txs"]:
            for input in transaction["inputs"]:
                if "prev_out" in input and "addr" in input["prev_out"]:
                    if "tumbler" in input["prev_out"]["addr"].lower() or "mixer" in input["prev_out"]["addr"].lower():
                        print("Tumbler or mixer detected in transaction", transaction["hash"])
    except ValueError:
        print("Invalid JSON response from API")
else:
    print("API request failed with status code", response.status_code)
