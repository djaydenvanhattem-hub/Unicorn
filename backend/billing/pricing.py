# id="pricing_v64"

PLANS = {
    "free": {
        "limit": 1000,
        "price": 0
    },
    "pro": {
        "limit": 10000,
        "price": 29
    },
    "enterprise": {
        "limit": None,
        "price": 99
    }
}


def get_plan(org_plan: str):
    return PLANS.get(org_plan, PLANS["free"])


def check_limits(org_plan: str, usage: int):
    plan = get_plan(org_plan)

    if plan["limit"] is None:
        return True, "unlimited"

    if usage >= plan["limit"]:
        return False, "limit reached"

    return True, "ok"
