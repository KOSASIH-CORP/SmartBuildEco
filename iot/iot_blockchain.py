import hashlib
import time

class IOTBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.mining_difficulty = 2

    def create_genesis_block(self):
        block = {
            'index': 0,
            'previous_hash': '0',
            'timestamp': time.time(),
            'transactions': []
        }
        self.chain.append(block)

    def create_new_block(self, previous_hash):
        block = {
            'index': len(self.chain),
            'previous_hash': previous_hash,
            'timestamp': time.time(),
            'transactions': self.pending_transactions
        }
        self.pending_transactions = []
        return block

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self, block):
        block_hash = self.calculate_hash(block)
        while not block_hash.startswith('0' * self.mining_difficulty):
            block['nonce'] += 1
            block_hash = self.calculate_hash(block)
        self.chain.append(block)

    def calculate_hash(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Example usage:
iot_bc = IOTBlockchain()
iot_bc.create_genesis_block()
iot_bc.add_transaction({'sender': 'Alice', 'recipient': 'Bob', 'amount': 10})
iot_bc.add_transaction({'sender': 'Bob', 'recipient': 'Alice', 'amount': 5})
block = iot_bc.create_new_block(iot_bc.chain[-1]['hash'])
iot_bc.mine_block(block)
print(iot_bc.chain)
