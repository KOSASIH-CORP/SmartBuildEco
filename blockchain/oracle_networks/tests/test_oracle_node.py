import unittest
from oracle_node import OracleNode

class TestOracleNode(unittest.TestCase):
    def test_process_block(self):
        oracle_node = OracleNode('node-1', 'https://example.com/blockchain')
        block = {'block_number': 1, 'transactions': []}
        block_hash = oracle_node.process_block(block)
        self.assertIsNotNone(block_hash)

    def test_get_block(self):
        oracle_node = OracleNode('node-1', 'https://example.com/blockchain')
        block = {'block_number': 1, 'transactions': []}
        block_hash =oracle_node.process_block(block)
        retrieved_block = oracle_node.get_block(block_hash)
        self.assertEqual(retrieved_block, block)

    def test_send_transaction(self):
        oracle_node = OracleNode('node-1', 'https://example.com/blockchain')
        transaction = {'from': '0x...UserAddress...', 'to': '0x...NodeAddress...', 'amount': 10}
        response = oracle_node.send_transaction(transaction)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
