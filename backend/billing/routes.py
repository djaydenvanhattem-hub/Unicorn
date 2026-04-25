from fastapi import APIRouter
from .stripe_service import create_customer, create_subscription

router = APIRouter()

@router.post("/billing/create")
def create(email: str):
    customer = create_customer(email)
    return {"customer_id": customer.id}

@router.post("/billing/subscribe")
def subscribe(customer_id: str, price_id: str):
    sub = create_subscription(customer_id, price_id)
    return {"subscription": sub.id}
