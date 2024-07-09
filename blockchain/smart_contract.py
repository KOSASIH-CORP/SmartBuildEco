import web3

def deploy_contract():
    # Deploy smart contract using Web3
    w3 = web3.Web3(web3.providers.InfuraProvider("https://mainnet.infura.io/v3/YOUR_PROJECT_ID"))
    contract = w3.eth.contract(abi="abi.json", bytecode="bytecode.hex")

    # Deploy contract
    tx_hash = contract.constructor().transact()

    return tx_hash
