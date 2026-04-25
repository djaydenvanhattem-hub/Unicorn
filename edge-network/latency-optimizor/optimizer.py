def optimize(latency):
    return "reroute" if latency > 100 else "stable"
