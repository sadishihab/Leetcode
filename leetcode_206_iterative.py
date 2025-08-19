# Reverse Linked List: iterative approach
# Iterate list. Reverse pointer at each node. Move prev & curr forward. Return prev.
# Time: O(n) — we traverse each node of the linked list exactly once
# Space: O(1) — only a few pointers (prev, current, next_node) are used regardless of list size

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        # Initialize previous as None and current as head
        prev = None
        current = head

        # Traverse the list
        while current is not None:

            next_node = current.next            # Store the next node
            current.next = prev                 # Reverse the link: point current's next to previous
            prev = current                      # Move prev and current one step forward
            current = next_node

        return prev                             # prev is the new head

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
