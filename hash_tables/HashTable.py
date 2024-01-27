from sympy import nextprime


class HashTable:
    """
    A class representing a hash table data structure.

    Attributes:
    - bucket_array (list): A list of buckets to store key-value pairs.
    - capacity (int): The current capacity of the hash table.
    - size (int): The number of key-value pairs stored in the hash table.
    - expansions (int): The number of times the hash table has been expanded.

    Methods:
    - __init__(self, initial_capacity=11): Initializes a new instance of the HashTable class.
    - hash(self, key, capacity=None): Computes the hash code for a given key.
    - insert(self, key, value): Inserts a key-value pair into the hash table.
    - search(self, key): Searches for a value in the hash table using the key.
    - delete(self, key): Deletes a key-value pair from the hash table using the key.
    - resize(self): Resizes the hash table to accommodate more key-value pairs.
    - report(self): Prints a report of the hash table's statistics and key-value pairs.
    """

    def __init__(self, initial_capacity=11):
        # chose 11 as the initial capacity
        # gets us started with a prime number:
        #     The reason for using prime numbers is that
        #     they are not the product of smaller numbers,
        #     which helps in spreading out the keys more evenly.
        # in a production environment with many accounts we would
        # choose a much larger prime number to load up the accounts
        self.bucket_array = [[] for _ in range(initial_capacity)]
        self.capacity = initial_capacity
        self.size = 0
        self.expansions = 0

    def hash(self, key, capacity=None):
        """
        Computes the hash code for a given key.

        Args:
        - key: The key to compute the hash code for.
        - capacity: The capacity of the hash table (optional).

        Returns:
        - The hash code for the given key.
        """
        if capacity is None:
            capacity = self.capacity
        #  double hashing logic
        primary_hash = hash(key)
        secondary_hash = 1 + primary_hash % (capacity - 1)
        return (primary_hash + secondary_hash) % capacity

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Args:
        - key: The key of the key-value pair.
        - value: The value of the key-value pair.
        """
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for item in bucket:
            if item[0] == key:
                item[1] = value  # Update the value if key already exists
                return
        if len(bucket) > 0:
            print(f"Collision occurred for key {key}. Resolving using chaining.")
        bucket.append((key, value))  # Use chaining to handle collisions
        self.size += 1
        if self.size > self.capacity * 0.7:
            self.resize()

    def search(self, key):
        """
        Searches for a value in the hash table using the key.

        Args:
        - key: The key to search for.

        Returns:
        - The value associated with the key if found, None otherwise.
        """
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for item in bucket:
            if item[0] == key:
                return item[1]  # Return the value if found
        return None  # Not found

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table using the key.

        Args:
        - key: The key of the key-value pair to delete.

        Returns:
        - The value of the deleted key-value pair if found, None otherwise.
        """
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for index, item in enumerate(bucket):
            if item[0] == key:
                del bucket[index]
                self.size -= 1
                return item[1]  # Return the deleted value
        return None  # Not found

    def resize(self):
        """
        Resizes the hash table to accommodate more key-value pairs.
        """
        self.expansions += 1
        # Calculate the new capacity using next prime number
        new_capacity = nextprime(self.capacity * 2)

        # Create a new bucket array with the new capacity
        new_bucket_array = [[] for _ in range(new_capacity)]

        # Iterate through each bucket in the old bucket array
        for bucket in self.bucket_array:
            # iterate through each key-value pair in each bucket
            for key, value in bucket:
                # Compute the new hash code using the new capacity
                new_hash_code = self.hash(key, new_capacity)

                # Append the key-value pair to the appropriate bucket in the new array
                new_bucket_array[new_hash_code].append((key, value))

        #  Update the hash table's attributes to the new values
        self.capacity = new_capacity
        self.bucket_array = new_bucket_array

    def report(self):
        """
        Prints a report of the hash table's statistics and key-value pairs.
        """
        print("HashTable Report")
        print("Total records:", self.size)
        print("Table Capacity:", self.capacity)
        print("Load Factor:", "{:.2f}".format(self.size / self.capacity))
        print("Total Expansions:", self.expansions)  # Print the number of expansions
        print("Records Detail:")

        for index, bucket in enumerate(self.bucket_array):
            for entry in bucket:
                customer_id, customer = entry
                # Combine bucket index and customer information on the same line
                formatted_balance = "${:.2f}".format(customer.balance)
                print(
                    f"   Bucket {index}: Customer ID: {customer_id}, Full Name: {customer.full_name}, Email: {customer.email}, Balance: {formatted_balance}"
                )

        print("End of Report\n")
