from database.models import User
from core.security import create_token

def authenticate(db, username, password):
    user = db.query(User).filter(User.username == username).first()

    if not user or user.password != password:
        return None

    return create_token({
        "user_id": user.id,
        "role": user.role
    })
