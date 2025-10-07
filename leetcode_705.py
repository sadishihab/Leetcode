class MyHashSet(object):
    """
    A simple HashSet implementation without using built-in set/dict.
    Uses separate chaining (list of lists) to handle collisions.
    """

    def __init__(self):
        self.capacity = 1000                                    # Total number of buckets (can be tuned for performance)
        self.buckets = [[] for _ in range(self.capacity)]       # Initialize all buckets as empty lists  # Each bucket stores keys that hash to the same index

    def _hash(self, key):
        """
        Hash function to map a key to a bucket index.
        Simple modulo-based hash.
        """
        return key % self.capacity

    def add(self, key):
        """
        Add a key to the HashSet if not already present.
        """
        index = self._hash(key)       # Find the bucket index
        bucket = self.buckets[index]  # Get the bucket list

        # Only add if key is not already in the bucket
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        """
        Remove a key from the HashSet if it exists.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Remove key if present
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        """
        Check if a key exists in the HashSet.
        Returns True if found, else False.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        return key in bucket
