import ecdsa

class WalletManager:
    def __init__(self):
        pass

    def generate_wallet(self):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key()
        address = hashlib.sha256(public_key.to_string()).hexdigest()[:-8]
        return private_key, public_key, address

    def sign_transaction(self, private_key, tx_hash):
        signature = private_key.sign(tx_hash)
        return signature
