def require_role(user_role, allowed):
    if user_role not in allowed:
        raise Exception("Unauthorized")
