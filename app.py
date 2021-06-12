from web3 import web3

ganache_url = "http://127.0.0.1:7545"
web3 = web3(web3.HttpProvider(ganache_url))

print(web3.isConnected)

