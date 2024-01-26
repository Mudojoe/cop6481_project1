from hash_tables.ProcessCommands import load_accounts
from hash_tables.ProcessCommands import process_commands


# Main function to start the application
def main():
    # Load test data into the hash table
    print("****Loading initial accounts****")
    hash_table = load_accounts("accountLoad.txt")
    print("****Initial accounts loaded.****")
    print("****Printing report after initial accounts loaded.****")
    hash_table.report()
    print("****Processing batch transaction file.****")
    process_commands("transactions.txt", hash_table)
    print("\n****Printing report after transactions.****")
    hash_table.report()


if __name__ == "__main__":
    main()
