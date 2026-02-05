class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle
            return None

        # Step 2: Find the start of the cycle
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow
