class MyHashMap:
    """
    HashMap implementation using separate chaining (list of lists).
    Each bucket stores key-value pairs as [key, value].
    """

    def __init__(self):
        self.capacity = 1000                    # Number of buckets
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """
        Simple hash function to map key to bucket index.
        """
        return key % self.capacity

    def put(self, key, value):
        """
        Insert a key-value pair or update existing key.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key exists → update
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # Else, append new key-value pair
        bucket.append([key, value])

    def get(self, key):
        """
        Return value associated with key, or -1 if not found.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        """
        Remove key from the map if it exists.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
