

from web3 import Web3
rpc_url="http://144.126.196.198:31920"
web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.isConnected()
private_key = '0x9ccac2d9cb08e106e616725eb93ae220b74e45f84fcba7'
account: LocalAccount = Account.from_key(private_key)
print(f"Your hot wallet address is {account.address}")
public_address='0x2F89F82055E803b470Da977C8260B4B25d0Fc43B'
balance = web3.eth.get_balance(public_address)
print(balance)
web3.default_account = account.address
target_contract='0x91FCa15f2602469894850ACEd90A6Fa523338e5d'
from web3.gas_strategies.rpc import rpc_gas_price_strategy
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
