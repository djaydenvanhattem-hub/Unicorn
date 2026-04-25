class BillingMesh:
    def calculate(self, usage):
        return usage["compute_hours"] * 0.12
