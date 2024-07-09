import hashlib

class ConsensusAlgorithm:
    def __init__(self):
        self.blockchain = []

    def validate_block(self, block):
        # Validate the block using the consensus algorithm
        pass

    def add_block(self, block):
        self.blockchain.append(block)

    def get_blockchain(self):
        return self.blockchain
