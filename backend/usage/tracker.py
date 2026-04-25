usage_store = {}

def track(org_id, metric):
    if org_id not in usage_store:
        usage_store[org_id] = 0

    usage_store[org_id] += 1

def get_usage(org_id):
    return usage_store.get(org_id, 0)
