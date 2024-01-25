from hash_tables.HashTable import HashTable
from hash_tables.Customer import Customer

def process_commands(filename, hash_table):
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into command and data parts
            command, data = line.strip().split(', ', 1)
            command = command.lower()

            if command == 'insert':
                # Further split the data part for the 'insert' command
                customer_id, full_name, email_balance = data.split(', ', 2)
                email, balance = email_balance.rsplit(', ', 1)

                customer = Customer(int(customer_id), full_name, email, float(balance))
                hash_table.insert(int(customer_id), customer)
                print(f"Inserted: {customer.full_name}")

            elif command == 'update':
                # Split the data part for the 'update' command
                customer_id, operation, amount = data.split(', ', 2)
                customer = hash_table.search(int(customer_id))
                if customer:
                    if operation.lower() == 'deposit':
                        customer.balance += float(amount)
                    elif operation.lower() == 'withdrawal':
                        customer.balance -= float(amount)
                    formatted_balance = "${:.2f}".format(customer.balance)
                    print(f"Updated: {customer.full_name}, New Balance: {formatted_balance}")

            elif command == 'find':
                # For the 'find' command, data is just the customer_id
                customer_id = data
                customer = hash_table.search(int(customer_id))
                if customer:
                    formatted_balance = "${:.2f}".format(customer.balance)
                    print(f"Found: Customer ID: {customer_id}, Full Name: {customer.full_name}, Email: {customer.email}, Balance: {formatted_balance}")
                else:
                    print(f"Customer ID: {customer_id} not found")

# End of ProcessCommands.py



def load_accounts(filename='accountLoad.txt'):
    hash_table = HashTable()
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split(', ')
            # The first part is the customer ID
            customer_id = int(parts[0])
            # The last two parts are email and balance
            email = parts[-2]
            balance = float(parts[-1])
            # The full name is everything else in the middle
            full_name = ', '.join(parts[1:-2])
            customer = Customer(customer_id, full_name, email, balance)
            hash_table.insert(customer.customer_id, customer)
    return hash_table
