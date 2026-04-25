class PolicyEngine:
    def is_allowed(self, user_role, action):
        rules = {
            "deploy": ["admin"],
            "read_logs": ["admin", "devops"],
            "ai_action": ["admin", "devops"]
        }
        return user_role in rules.get(action, [])
