class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_string(self):
        return f"Transaction from {self.sender} to {self.recipient} for {self.amount} units"
