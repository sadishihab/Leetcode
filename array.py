# Python arrays are dynamic by default, but this is an example of some methods and resizing.
#This initializes a dynamic array with a capacity of 2, a length of 0 (no elements), and a list self.arr filled with two zeros [0, 0].
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2                      # Array of capacity = 2

#Purpose: Adds an element n to the end of the array. # How it works: Checks if the array is full (self.length == self.capacity). If it is, calls resize() to double the capacity. Inserts n at the index self.length (the first empty position).Increments self.length to reflect the new element.
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

#Purpose: Doubles the array’s capacity when it’s full. # How it works: Doubles self.capacity (e.g., from 2 to 4). Creates a new list newArr with the new capacity, initialized with zeros. Copies all existing elements from self.arr to newArr. Replaces self.arr with newArr. # Why double?: Doubling the capacity (rather than increasing by a fixed amount) ensures amortized O(1) time complexity for insertions, a common strategy in dynamic arrays (like Python’s list).

    def resize(self):
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

#Purpose: Removes the last element from the array. # How it works: If the array has elements (self.length > 0), decrements self.length. The element at self.arr[self.length] is not explicitly cleared (e.g., set to 0), but it’s effectively ignored since self.length no longer counts it. No resizing is done to shrink the array (a design choice to avoid frequent resizing).

    def popback(self):
        if self.length > 0:
            self.length -= 1

#Purpose: Returns the element at index i. #How it works: Checks if i is valid (less than self.length). If valid, returns self.arr[i]. If invalid, rasie an exception

    def get(self, i):
        if i < self.length:
            return self.arr[i]
        raise IndexError("Index out of bounds")

#Purpose: Inserts (or overwrites) the element at index i with value n. # How it works: If i is within bounds (i < self.length), sets self.arr[i] = n. Does not shift elements or increase length, so it overwrites the existing value at i. If i is out of bounds, an exception would be thrown. Note: This is not a typical “insert” operation for arrays, which usually shifts elements to make room for n at index i. This implementation just overwrites.

    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
        raise IndexError("Index out of bound")

#Purpose: Prints all elements in the array (up to self.length).#How it works: Iterates from 0 to self.length - 1 and prints each element. Adds a newline at the end for clean output.

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()

arr = Array()
arr.pushback(5)
arr.pushback(10)
arr.print()