class Customer:
    """
    Represents a customer with their ID, full name, email, and balance.
    """

    def __init__(self, customer_id, full_name, email, balance):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.balance = balance
