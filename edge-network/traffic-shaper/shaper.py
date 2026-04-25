def shape_traffic(load):
    return "throttle" if load > 0.8 else "normal"
