import stripe

stripe.api_key = "sk_test_key"

def create_customer(email):
    return stripe.Customer.create(email=email)

def create_subscription(customer_id, price_id):
    return stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}]
    )
