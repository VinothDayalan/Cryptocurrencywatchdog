import requests
import json

txid = "0x48805dfdd5e452e0b068042e734d2ee8097c81eb9a0aa94b8ac9462008650c62"  # Replace with the transaction ID you want to check

api_endpoint = f"https://blockstream.info/api/tx/{txid}"
response = requests.get(api_endpoint)
# Check if the transaction was found
if response.status_code != 200:
    # If the transaction was not found, print an error message
    print(f"Error retrieving transaction details. Status code: {response.status_code}")
else:
    # If the transaction was found, parse the JSON response
    data = json.loads(response.content)
    # Check if the transaction has inputs or outputs with non-zero values
    is_tumbled = False
    for input in data["vin"]:
        # Check if the input is a coinbase transaction
        prev_out = input["prevout"]
        if "scriptpubkey_address" in prev_out and ("tumbler" in prev_out["scriptpubkey_address"].lower() or "mixer" in prev_out["scriptpubkey_address"].lower()):
            # If the input is a coinbase transaction, print a message
            is_tumbled = True
            break
    # If the transaction is not a coinbase transaction, check the outputs
    if is_tumbled:
        # If the transaction is a coinbase transaction, print a message
        print(f"Transaction {txid} is a mixed or tumbled transaction.")
    else:
        # If the transaction is not a coinbase transaction, print a message
        print(f"Transaction {txid} is not a mixed or tumbled transaction.")
