import hashlib
import time

class Miner:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.difficulty = 2

    def mine_block(self, block):
        block_hash = self.calculate_hash(block)
        while not block_hash.startswith('0' * self.difficulty):
            block['nonce'] += 1
            block_hash = self.calculate_hash(block)
        self.blockchain.append(block)
        return block_hash

    def calculate_hash(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
