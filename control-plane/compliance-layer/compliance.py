class ComplianceEngine:

    def __init__(self):
        self.rules = [
            "no_production_deploy_without_approval",
            "log_all_actions",
            "restrict_high_risk_regions"
        ]

    def validate_action(self, action, context):
        if action == "deploy" and not context.get("approved"):
            return False, "Deployment requires approval"

        if context.get("region") == "restricted":
            return False, "Region is restricted"

        return True, "Allowed"
