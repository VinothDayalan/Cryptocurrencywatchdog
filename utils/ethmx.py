from web3 import Web3

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/7bc81474ae5c47d79e5e09a837dde5bf'))


# Mixer contract ABI
mixer_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_hash", "type": "bytes32"}],
        "name": "isTransactionProcessed",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Mixer contract address
mixer_address = Web3.toChecksumAddress('0x248b6928674b1e452d908f9aadea866a6dc4de67')

# Instantiate mixer contract
mixer_contract = web3.eth.contract(address=mixer_address, abi=mixer_abi)

# Check if a transaction has been processed by the mixer
tx_hash = '0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
is_processed = mixer_contract.functions.isTransactionProcessed(tx_hash).call()
print(is_processed)
