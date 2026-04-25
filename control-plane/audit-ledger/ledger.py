import hashlib

ledger = []

def log(event):
    entry = {
        "event": event,
        "hash": hashlib.sha256(str(event).encode()).hexdigest()
    }
    ledger.append(entry)
