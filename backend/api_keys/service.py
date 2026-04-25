import secrets

api_keys = {}

def create_key(org_id):
    key = secrets.token_hex(16)
    api_keys[key] = org_id
    return key

def validate_key(key):
    return api_keys.get(key)
