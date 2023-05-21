import blockcypher

# Set the API token (optional)
blockcypher.api_key = "12bf38cf3ee8422296b0f50ead946a34"

# Retrieve the transaction data from the Bitcoin network
txid = input("Enter the transaction ID: ")
tx = blockcypher.get_transaction_details(txid)

# Check if the transaction has inputs or outputs with non-zero values
if any(i['output_value'] == 0 for i in tx['inputs']) or any(o['value'] == 0 for o in tx['outputs']):
    print('This transaction may have been mixed or passed through a tumbler.')
else:
    print('This transaction does not appear to have been mixed or passed through a tumbler.')
