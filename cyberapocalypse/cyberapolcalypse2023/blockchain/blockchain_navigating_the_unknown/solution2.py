from web3 import Web3, HTTPProvider
import json
w3 = Web3(Web3.HTTPProvider("http://144.126.196.198:31920"))
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3.is_Connected())
