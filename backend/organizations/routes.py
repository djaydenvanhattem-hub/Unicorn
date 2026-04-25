from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from .models import Organization

router = APIRouter()

@router.post("/orgs")
def create_org(name: str, db: Session = Depends(get_db)):
    org = Organization(name=name)
    db.add(org)
    db.commit()
    return {"org_id": org.id}
