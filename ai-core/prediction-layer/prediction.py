def predict(metrics):
    return "risk_low" if metrics["error_rate"] < 0.05 else "risk_high"
