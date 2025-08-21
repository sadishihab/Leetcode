class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reverseList(self, head):
#         if not head or not head.next:           # Base case: empty list or single node
#             return head
#         new_head = self.reverseList(head.next)  # Recursively reverse the rest of the list
#         head.next.next = head                   # Reverse the current node's pointer
#         head.next = None
#
#         return new_head

class Solution:
    def reverseList(self, head):
        if not head or not head.next:  # Base case
            print(f"Base case reached: head = {head.val if head else None}")
            return head

        print(f"Recursing: head = {head.val}, head.next = {head.next.val}")

        new_head = self.reverseList(head.next)  # Recurse

        print(f"Before reversing pointer: head = {head.val}, head.next = {head.next.val}, new_head = {new_head.val}")

        head.next.next = head  # Reverse pointer
        head.next = None

        print(f"After reversing pointer: head = {head.val}, head.next = {head.next}, new_head = {new_head.val}")

        return new_head


# Create a sample list: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Instantiate solution and test
solution = Solution()
new_head = solution.reverseList(head)

# Print result
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
print("None")  # Output: 3 -> 2 -> 1 -> None