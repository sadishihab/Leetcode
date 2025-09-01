class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        # Use a dummy node for simplicity
        self.head = self.tail = ListNode(-1)

    def enqueue(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head.next:  # Queue is empty
            return None

        val = self.head.next.val
        self.head.next = self.head.next.next

        # If queue becomes empty, reset tail to dummy head
        if not self.head.next:
            self.tail = self.head

        return val

    def print_queue(self):
        cur = self.head.next
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.print_queue()  # 10 -> 20 -> 30 -> None

print(q.dequeue())  # 10
q.print_queue()     # 20 -> 30 -> None

print(q.dequeue())  # 20
print(q.dequeue())  # 30
print(q.dequeue())  # None (empty queue)
