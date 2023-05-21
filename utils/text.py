import requests
import json

API_ENDPOINT = "https://api.blockchain.info/v2/"
txid = "8b6a830c6a70391b2c647dc9f9dd04ce40ab893af4176a694b1a3a3c8783c584"
method = "rawtx/" + txid + "?format=json"
response = requests.get(API_ENDPOINT + method)

data = json.loads(response.content)
if "inputs" in data and "out" in data:
    for input in data["inputs"]:
        if "prev_out" in input and "addr" in input["prev_out"]:
            if "tumbler" in input["prev_out"]["addr"].lower() or "mixer" in input["prev_out"]["addr"].lower():
                print("Tumbler or mixer detected in transaction", txid)
                break
    else:
        for output in data["out"]:
            if "addr" in output:
                if "tumbler" in output["addr"].lower() or "mixer" in output["addr"].lower():
                    print("Tumbler or mixer detected in transaction", txid)
                    break
        else:
            print("Transaction", txid, "is not a mixed or tumbled transaction")
else:
    print("Transaction", txid, "not found")
