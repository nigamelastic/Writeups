from web3 import Web3

from solcx import compile_source
from web3.contract import ConciseContract

# Replace with the RPC URL of your private chain node

rpc_url = 'http://161.35.168.118:30913'
# Replace with your private key and the target contract address
private_key = "0xfb024340f8ea6b6ad96afb16fa33ed5f7eddf25b132a6546cdfd65c83f2ac7f5"
target_contract_address = "0x75BA682316f7dE19e6BC91Cfa80b2CE43Ff548A8"

# Connect to the private chain node
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Set the default account to your address
web3.eth.defaultAccount = "0xb925B280bA97cA38f9896A1e5732a52f44C0c088"

# Load your account using your private key
account = web3.eth.account.privateKeyToAccount(private_key)

# Compile the source code of the Setup contract
setup_source_code = """
pragma solidity ^0.8.18;

import {Unknown} from "./Unknown.sol";

contract Setup {
    Unknown public immutable TARGET;

    constructor() {
        TARGET = new Unknown();
    }

    function isSolved() public view returns (bool) {
        return TARGET.updated();
    }
}
"""
setup_compiled = compile_source(setup_source_code)

# Get the bytecode and ABI of the Setup contract
setup_bytecode = setup_compiled["<stdin>:Setup"]["bin"]
setup_abi = setup_compiled["<stdin>:Setup"]["abi"]

# Deploy the Setup contract
Setup = web3.eth.contract(abi=setup_abi, bytecode=setup_bytecode)
nonce = web3.eth.getTransactionCount(account.address)
gas_price = web3.eth.gasPrice
gas_limit = 5000000  # Replace with the gas limit for your transaction
tx = Setup.constructor().buildTransaction({
    "nonce": nonce,
    "gas": gas_limit,
    "gasPrice": gas_price
})
signed_tx = account.signTransaction(tx)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
setup_contract_address = tx_receipt.contractAddress

# Get the ABI of the Unknown contract
unknown_abi = '''
[
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "version",
                "type": "uint256"
            }
        ],
        "name": "updateSensors",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "updated",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
'''

# Create a contract object for the Unknown contract
unknown_contract = web3.eth.contract(address=target_contract_address, abi=unknown_abi)

# Create a contract object for the Setup contract
setup_contract = web3.eth.contract(address=setup_contract_address, abi=setup_abi)

# Verify that the Setup contract is set up properly
assert setup_contract.functions.isSolved().call()

# Call the updateSensors function of the Unknown contract
tx_hash = unknown_contract
