# id="chaos_v63"
import random

def simulate():
    return random.choice([
        "kill_pod",
        "network_delay",
        "cpu_spike"
    ])
