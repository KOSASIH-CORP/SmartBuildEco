import requests

class BlockchainExplorer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://blockchain-explorer.com/api'

    def get_block_info(self, block_hash):
        response = requests.get(f'{self.base_url}/block/{block_hash}', headers={'API-Key': self.api_key})
        return response.json()

    def get_transaction_info(self, tx_hash):
        response = requests.get(f'{self.base_url}/tx/{tx_hash}', headers={'API-Key': self.api_key})
        return response.json()

    def get_address_info(self, address):
        response = requests.get(f'{self.base_url}/address/{address}', headers={'API-Key': self.api_key})
        return response.json()
