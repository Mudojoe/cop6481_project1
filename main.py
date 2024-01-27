from hash_tables.ProcessCommands import load_accounts
from hash_tables.ProcessCommands import process_commands


# Main function to start the application
def main():
    # Load test data into the hash table
    accounts_file_name = "accountLoad.txt"
    print(f"****Loading initial accounts from file '{accounts_file_name}'****")
    hash_table = load_accounts(accounts_file_name)
    print("****Initial accounts load complete.****\n")
    print("****Dump of hash table and stats after initial load.****")
    hash_table.report()
    batch_transactions_file  = "transactions.txt"
    print(f"***\n****Processing batch transactions from file '{batch_transactions_file}'.****\n***")
    process_commands(batch_transactions_file, hash_table)
    print("\n****Printing report after processing batch transactions.****")
    hash_table.report()


if __name__ == "__main__":
    main()
