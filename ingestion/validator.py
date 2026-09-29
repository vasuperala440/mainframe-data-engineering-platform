def validate_customer(customer):
    if not customer["customer_id"]:
        return False

    if not customer["customer_name"]:
        return False

    if not customer["state"]:
        return False

    return True

customer = {
    "customer_id": "C000001",
    "customer_name": "John Smith",
    "state": "TX"
}

print(validate_customer(customer))

bad_customer = {
    "customer_id": "",
    "customer_name": "John Smith",
    "state": "TX"
}

print(validate_customer(bad_customer))