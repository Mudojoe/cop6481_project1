from sympy import nextprime
class HashTable:
    def __init__(self, initial_capacity=11):
        # chose 11 as the initial capacity
        # for this project is small enough for an initial capacity
        # yet it gets us started with a prime number:
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
        if capacity is None:
            capacity = self.capacity

        # Same double hashing logic as before, but using the provided capacity
        primary_hash = hash(key)
        secondary_hash = 1 + primary_hash % (capacity - 1)
        return (primary_hash + secondary_hash) % capacity

    def insert(self, key, value):
        # Insert a value into the hash table using the key
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for item in bucket:
            if item[0] == key:
                item[1] = value  # Update the value if key already exists
                return
        bucket.append((key, value))  # Use chaining to handle collisions
        self.size += 1
        if self.size > self.capacity * 0.7:
            self.resize()

    def search(self, key):
        # Search for a value in the hash table using the key
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for item in bucket:
            if item[0] == key:
                return item[1]  # Return the value if found
        return None  # Not found

    def delete(self, key):
        # Delete a value from the hash table using the key
        hash_code = self.hash(key)
        bucket = self.bucket_array[hash_code]
        for index, item in enumerate(bucket):
            if item[0] == key:
                del bucket[index]
                self.size -= 1
                return item[1]  # Return the deleted value
        return None  # Not found

    def resize(self):
        self.expansions += 1
        # Step 1: Calculate the new capacity
        new_capacity = nextprime(self.capacity * 2)

        # Step 2: Create a new bucket array with the new capacity
        new_bucket_array = [[] for _ in range(new_capacity)]

        # Step 3: Iterate through each bucket in the old bucket array
        for bucket in self.bucket_array:
            # Step 4: Iterate through each key-value pair in each bucket
            for key, value in bucket:
                # Step 5: Compute the new hash code using the new capacity
                new_hash_code = self.hash(key, new_capacity)

                # Step 6: Append the key-value pair to the appropriate bucket in the new array
                new_bucket_array[new_hash_code].append((key, value))

        # Step 7: Update the hash table's attributes to the new values
        self.capacity = new_capacity
        self.bucket_array = new_bucket_array
        # The size of the hash table remains unchanged

        # ... (inside the HashTable class)

    def report(self):
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
                    f"   Bucket {index}: Customer ID: {customer_id}, Full Name: {customer.full_name}, Email: {customer.email}, Balance: {formatted_balance}")

        print("End of Report\n")

        # ... (other parts of the HashTable class)

