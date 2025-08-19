# Node class for singly linked list
class ListNode:
    def __init__(self, val):
        self.val = val       # Value stored in the node
        self.next = None     # Pointer to the next node (None by default)

# Singly linked list implementation
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)  # Dummy head node to simplify insertions/removals
        self.tail = self.head      # Initially, tail points to the dummy head

    # Insert a new node at the end of the list
    def insert_end(self, val):
        new_node = ListNode(val)   # Create a new node with the given value
        self.tail.next = new_node  # Link the current tail node to the new node
        self.tail = new_node       # Update tail to point to the new last node

    # Remove a node at a given 0-based index
    def remove(self, index):
        curr = self.head           # Start from dummy head
        # Move curr to the node **just before** the one we want to remove
        for _ in range(index):
            if not curr.next:      # If index is out of range, do nothing
                return
            curr = curr.next
        # Remove the target node if it exists
        if curr.next:
            curr.next = curr.next.next  # Skip the target node
            # If we removed the last node, update tail to the previous node
            if curr.next is None:
                self.tail = curr

    # Print the linked list in a readable format
    def print_list(self):
        curr = self.head.next        # Skip dummy head
        nodes = []                   # Temporary list to store node values
        while curr:
            nodes.append(str(curr.val))  # Convert node value to string and append
            curr = curr.next
        # Join all node values with ' -> ' and show that the list ends with None
        print(" -> ".join(nodes) + ' -> None')



def test_linked_list():
    ll = LinkedList()

    # Insert nodes
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    ll.insert_end(40)
    print("After inserting 10, 20, 30, 40:")
    ll.print_list()  # Expected: 10 -> 20 -> 30 -> 40 -> None

    # Remove a middle node (index 1 → value 20)
    ll.remove(1)
    print("After removing index 1 (value 20):")
    ll.print_list()  # Expected: 10 -> 30 -> 40 -> None

    # Remove first node (index 0 → value 10)
    ll.remove(0)
    print("After removing index 0 (value 10):")
    ll.print_list()  # Expected: 30 -> 40 -> None

    # Remove last node (index 1 → value 40)
    ll.remove(1)
    print("After removing last node (value 40):")
    ll.print_list()  # Expected: 30 -> None
    print("Tail value:", ll.tail.val)  # Expected: 30

    # Remove out-of-range index (index 5)
    ll.remove(5)
    print("After removing out-of-range index 5:")
    ll.print_list()  # Expected: 30 -> None (unchanged)

    # Remove remaining node (index 0 → value 30)
    ll.remove(0)
    print("After removing the last remaining node:")
    ll.print_list()  # Expected: empty
    print("Tail value:", ll.tail.val)  # Expected: -1 (dummy head)

# Run the test
test_linked_list()









