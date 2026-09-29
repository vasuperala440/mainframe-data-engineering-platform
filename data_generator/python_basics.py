def calculate_transaction(amount, tax):
    # return final amount
    final_amount = amount+tax
    return(final_amount)

print(calculate_transaction(100,5))


customers = [
    {
        "customer_id": "C000001",
        "customer_name": "John Smith",
        "state": "TX"
    },
    {
        "customer_id": "C000002",
        "customer_name": "Mary Johnson",
        "state": "CA"
    },
    {
        "customer_id": "C000003",
        "customer_name": "David Brown",
        "state": "NY"
    }
]

for customer in customers:
    print(customer["customer_id"], customer["customer_name"])



def get_customers_by_state(customers, state):
    for customer in customers:
        if customer["state"] == state:
            return(customer)

texas_customers = get_customers_by_state(customers, "TX")

print(texas_customers)