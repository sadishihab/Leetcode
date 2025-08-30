class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

        # Optimized traversal

    def _getNode(self, index):
        if index < self.size // 2:  # start from head
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:  # start from tail
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        return self._getNode(index).val


    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1


    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        curr = self._getNode(index)
        new_node = ListNode(val)
        new_node.next = curr
        new_node.prev = curr.prev
        curr.prev.next = new_node
        curr.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        curr = self._getNode(index)
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1


    def print_list(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, end = ' -> ')
            curr = curr.next


dll = MyLinkedList()
dll.addAtHead(1)
dll.addAtTail(3)
dll.addAtIndex(1, 2)
print(dll.get(1))
dll.deleteAtIndex(1)
print(dll.get(1))


dll.print_list()



