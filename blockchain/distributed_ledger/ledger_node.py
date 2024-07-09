import hashlib
import socket

class LedgerNode:
    def __init__(self, node_id, node_address):
        self.node_id = node_id
        self.node_address = node_address
        self.ledger = []

    def connect_to_node(self, node_address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((node_address, 8080))
        return sock

    def send_transaction(self, transaction):
        transaction_hash = hashlib.sha256(transaction.encode()).hexdigest()
        self.ledger.append(transaction_hash)
        return transaction_hash

    def verify_transaction(self, transaction_hash):
        if transaction_hash in self.ledger:
            return True
        return False
