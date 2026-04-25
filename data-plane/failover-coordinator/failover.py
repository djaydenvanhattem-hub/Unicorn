def failover(region_status):
    if region_status["eu"] == "down":
        return "failover_to_us"
