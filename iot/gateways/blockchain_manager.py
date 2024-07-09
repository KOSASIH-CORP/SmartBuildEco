import hashlib
from blockchain import Blockchain

class BlockchainManager:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def create_block(self, data):
        block = self.blockchain.create_block(data)
        return block

    def add_block(self, block):
        self.blockchain.add_block(block)

    def verify_chain(self):
        return self.blockchain.verify_chain()

    def get_block(self, block_hash):
        return self.blockchain.get_block(block_hash)

# Example usage:
blockchain = Blockchain()
blockchain_manager = BlockchainManager(blockchain)
data = {'temperature': 25, 'humidity': 60}
block = blockchain_manager.create_block(data)
blockchain_manager.add_block(block)
print(blockchain_manager.verify_chain())
block_hash = blockchain_manager.get_block(block.hash)
print(block_hash)
