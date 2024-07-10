import hashlib
import json
import requests

class OracleNode:
    def __init__(self, node_id, blockchain_url):
        self.node_id = node_id
        self.blockchain_url = blockchain_url
        self.data_store = {}

    def process_block(self, block):
        block_hash = hashlib.sha256(json.dumps(block).encode()).hexdigest()
        self.data_store[block_hash] = block
        return block_hash

    def get_block(self, block_hash):
        return self.data_store.get(block_hash)

    def send_transaction(self, transaction):
        response = requests.post(self.blockchain_url + '/transactions', json=transaction)
        return response.json()

oracle_node = OracleNode('node-1', 'https://example.com/blockchain')
