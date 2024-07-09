import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.mining_difficulty = 3

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
        hash = self.calculate_hash(block)
        while not hash.startswith('0' * self.mining_difficulty):
            block['nonce'] += 1
            hash = self.calculate_hash(block)
        self.chain.append(block)

    def calculate_hash(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def get_chain(self):
        return self.chain

# Example usage:
bc = Blockchain()
bc.create_genesis_block()
bc.add_transaction({'from': 'Alice', 'to': 'Bob', 'amount': 10})
bc.add_transaction({'from': 'Bob', 'to': 'Charlie', 'amount': 5})
block = bc.create_new_block(bc.chain[-1]['hash'])
bc.mine_block(block)
print(bc.get_chain())
