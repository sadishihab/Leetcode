class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMap:
    # Unique marker object for deleted slots
    DELETED = object()

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None] * self.capacity

    # Simple hash function based on ASCII values of characters
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    # Get the value associated with a key
    def get(self, key):
        index = self.hash(key)
        start_index = index  # to avoid infinite loop

        while self.map[index] is not None:
            # Only check non-deleted slots
            if self.map[index] != self.DELETED and self.map[index].key == key:
                return self.map[index].val
            index = (index + 1) % self.capacity
            # If we circled back, key does not exist
            if index == start_index:
                break
        return None

    # Insert or update a key-value pair
    def put(self, key, val):
        index = self.hash(key)
        start_index = index  # to avoid infinite loop

        while True:
            # Insert into empty or deleted slot
            if self.map[index] is None or self.map[index] == self.DELETED:
                self.map[index] = Pair(key, val)
                self.size += 1
                # Rehash if load factor >= 0.5
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            # Update value if key already exists
            elif self.map[index] != self.DELETED and self.map[index].key == key:
                self.map[index].val = val
                return
            # Move to next slot
            index = (index + 1) % self.capacity
            # If we circled back, map is full (shouldn't happen with rehashing)
            if index == start_index:
                raise Exception("HashMap is full")

    # Remove a key from the map
    def remove(self, key):
        if self.get(key) is None:
            return

        index = self.hash(key)
        start_index = index                     # remember where we started

        while True:
            if self.map[index] != self.DELETED and self.map[index].key == key:
                # Instead of None, use DELETED marker to avoid breaking probing chains
                self.map[index] = self.DELETED
                self.size -= 1
                return
            index = (index + 1) % self.capacity
            if index == start_index:
                break                           # we circled back → key does not exist

    # Rehash the map (double capacity and reinsert all existing keys)
    def rehash(self):
        old_map = self.map
        self.capacity *= 2  # Doubling capacity (can use prime numbers for better distribution)
        self.map = [None] * self.capacity
        self.size = 0

        for pair in old_map:
            if pair and pair != self.DELETED:
                self.put(pair.key, pair.val)

    # Print all key-value pairs
    def print(self):
        for pair in self.map:
            if pair and pair != self.DELETED:
                print(pair.key, pair.val)
