# 1. Import the gas strategy
from web3.gas_strategies.rpc import rpc_gas_price_strategy

# 2. Add the Web3 provider logic here:
# {...}

# 3. Create address variables
account_from = {
    "private_key": "0x9ccac2d9cb08e106e616725eb93ae220b74e45f84fcba7144385cbbf50be4287",
    "address": "0x2F89F82055E803b470Da977C8260B4B25d0Fc43B",
}
address_to = "0x91FCa15f2602469894850ACEd90A6Fa523338e5d"

print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)

# 4. Set the gas price strategy
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

# 5. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(
    {
        "nonce": web3.eth.get_transaction_count(account_from["address"]),
        "gasPrice": web3.eth.generate_gas_price(),
        "gas": 21000,
        "to": address_to,
        "value": web3.toWei("1", "ether"),
    },
    account_from["private_key"],
)

# 6. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")

