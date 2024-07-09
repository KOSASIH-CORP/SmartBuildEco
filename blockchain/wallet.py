import hashlib
import ecdsa

class Wallet:
    def __init__(self, private_key):
        self.private_key = private_key
        self.public_key = self.generate_public_key()
        self.address = self.generate_address()

    def generate_public_key(self):
        public_key = ecdsa.VerifyingKey.from_string(self.private_key, curve=ecdsa.SECP256k1).to_string()
        return public_key

    def generate_address(self):
        address = hashlib.sha256(self.public_key).hexdigest()[:-8]
        return address

    def sign_transaction(self, tx_hash):
        signature = ecdsa.SigningKey.from_string(self.private_key, curve=ecdsa.SECP256k1).sign(tx_hash)
        return signature
