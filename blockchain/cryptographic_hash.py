import hashlib

class CryptographicHash:
    def __init__(self):
        pass

    def sha256(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def keccak256(self, data):
        return hashlib.keccak_256(data.encode()).hexdigest()
