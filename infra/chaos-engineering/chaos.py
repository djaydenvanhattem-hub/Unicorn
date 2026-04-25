import random

def inject_failure():
    return random.choice(["latency", "node_failure", "packet_loss"])
