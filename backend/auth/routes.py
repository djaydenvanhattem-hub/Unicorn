from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.schemas import UserCreate, UserLogin
from database.models import User
from auth.service import authenticate

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        password=user.password,
        role="devops"
    )
    db.add(new_user)
    db.commit()
    return {"status": "created"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate(db, user.username, user.password)
    if not token:
        return {"error": "invalid creds"}
    return {"token": token}
