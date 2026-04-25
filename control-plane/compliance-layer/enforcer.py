from .compliance import ComplianceEngine
from control-plane.audit-ledger.ledger import log

engine = ComplianceEngine()

def enforce(action, context):
    allowed, reason = engine.validate_action(action, context)

    log({
        "action": action,
        "context": context,
        "allowed": allowed,
        "reason": reason
    })

    return allowed
