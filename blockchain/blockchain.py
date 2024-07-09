class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def add_block(self, block):
        self.chain.append(block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner):
        if not self.pending_transactions:
            return
        block = {'transactions': self.pending_transactions, 'nonce': 0}
        block_hash = miner.mine_block(block)
        self.add_block({'hash': block_hash, 'transactions': self.pending_transactions})
        self.pending_transactions = []
