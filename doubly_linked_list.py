class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node

    def insert_end(self, val):
        new_node = ListNode(val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    # Remove first node after dummy head
    def remove_front(self):
        # checking if the list is empty
        if self.head.next == self.tail:
            print('List is empty')
            return

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail
    def remove_end(self):
        # Checking if the list is empty
        if self.head.next == self.tail:
            print('List is empty')
            return

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print_list(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, end = ' -> ')
            curr = curr.next

dll = LinkedList()
dll.insert_front(10)
dll.insert_end(20)
dll.insert_front(5)
# dll.remove_end()
# dll.remove_front()
dll.print_list()

