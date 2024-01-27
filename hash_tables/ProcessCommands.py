from hash_tables.HashTable import HashTable
from hash_tables.Customer import Customer


def process_commands(filename, hash_table):
    """
    Processes commands from a file and applies them to a hash table.

    Args:
        filename (str): The name of the file containing the commands.
        hash_table (HashTable): The hash table to apply the commands to.
    """
    with open(filename, "r") as file:
        for line in file:
            # Split the line into command and data parts
            print("\nProcessing batch record: {}".format(line.strip()))
            command, data = line.strip().split(", ", 1)
            command = command.lower()

            if command == "insert":
                print("Adding new account (Insert)")
                process_insert_command(data, hash_table)

            elif command == "update":
                print("Processing 'update' command")
                process_update_command(data, hash_table)

            elif command == "find":
                print("Processing command to find the account")
                process_find_command(data, hash_table)


def process_insert_command(data, hash_table):
    """
    Processes an insert command and applies it to a hash table.

    Args:
        data (str): The data for the insert command, formatted as "customer_id, full_name, email, balance".
        hash_table (HashTable): The hash table to insert the new customer into.
    """
    parts = data.strip().split(", ")
    customer_id = parts[0]
    email = parts [-2]
    balance = parts[-1]
    full_name = ", ".join(parts[1:-2])
    print(f"New customer name : {full_name}, account number {customer_id}")
    customer = Customer(int(customer_id), full_name, email, float(balance))
    hash_table.insert(int(customer_id), customer)

def process_update_command(data, hash_table):
    """
    Processes an update command and applies it to a hash table.

    Args:
        data (str): The data for the update command, formatted as "customer_id, operation, amount".
        hash_table (HashTable): The hash table to update the customer in.
    """
    customer_id, operation, amount = data.split(", ", 2)

    customer = hash_table.search(int(customer_id))
    if customer:
        #print(f"previous balance={customer.balance}, update amount = {amount}")
        print(f"previous balance=${customer.balance:.2f}, update amount = ${float(amount):.2f}")
        if operation.lower() == "deposit":
            customer.balance += float(amount)
            print(f"This is a deposit")
        elif operation.lower() == "withdrawal":
            customer.balance -= float(amount)
            print(f"This is a withdrawal")
        formatted_balance = "${:.2f}".format(customer.balance)
        print(f"Updated: {customer.full_name}, New Balance: {formatted_balance}")


def process_find_command(data, hash_table):
    """
    Processes a find command and applies it to a hash table.

    Args:
        data (str): The data for the find command, formatted as "customer_id".
        hash_table (HashTable): The hash table to find the customer in.
    """
    customer_id = data
    customer = hash_table.search(int(customer_id))
    if customer:
        formatted_balance = "${:.2f}".format(customer.balance)
        print(f"Found:\n    Customer ID : {customer_id}\n    Full Name: {customer.full_name}")
        print(f"    Email: {customer.email}\n    Current Balance: {formatted_balance}")
    else:
        print(f"Customer ID: {customer_id} not found")


# End of ProcessCommands.py


def load_accounts(filename="accountLoad.txt"):
    """
    Loads customer accounts from a file and inserts them into a hash table.

    Args:
        filename (str): The name of the file to load accounts from. Default is 'accountLoad.txt'.

    Returns:
        HashTable: The hash table containing the loaded customer accounts.
    """
    hash_table = HashTable()
    with open(filename, "r") as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split(", ")
            # The first part is the customer ID
            customer_id = int(parts[0])
            # The last two parts are email and balance
            email = parts[-2]
            balance = float(parts[-1])
            # The full name is everything else in the middle
            full_name = ", ".join(parts[1:-2])
            customer = Customer(customer_id, full_name, email, balance)
            hash_table.insert(customer.customer_id, customer)
    return hash_table
