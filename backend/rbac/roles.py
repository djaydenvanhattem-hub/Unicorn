def require_role(user, allowed):
    return user["role"] in allowed
