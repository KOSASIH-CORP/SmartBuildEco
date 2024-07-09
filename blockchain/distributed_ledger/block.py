class Block:
    def __init__(self, transactions, previous_block_hash):
        self.transactions = transactions
        self.previous_block_hash = previous_block_hash
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.transactions, sort_keys=True) + self.previous_block_hash
        return hashlib.sha256(block_string.encode()).hexdigest()
