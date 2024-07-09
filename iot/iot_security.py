import hashlib
import hmac

class IOTSecurity:
    def __init__(self):
        self.secret_key = 'secret_key_here'

    def generate_hash(self, data):
        hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return hash

    def generate_hmac(self, data):
        hmac_obj = hmac.new(self.secret_key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256)
        hmac_digest = hmac_obj.hexdigest()
        return hmac_digest

    def verify_hmac(self, data, hmac_digest):
        expected_hmac = self.generate_hmac(data)
        if hmac_digest == expected_hmac:
            return True
        return False

# Example usage:
iot_sec = IOTSecurity()
data = 'Hello, IoT security!'
hash = iot_sec.generate_hash(data)
hmac_digest = iot_sec.generate_hmac(data)
print(f'Hash: {hash}, HMAC: {hmac_digest}')
if iot_sec.verify_hmac(data, hmac_digest):
    print('HMAC is valid')
else:
    print('HMAC is invalid')
