class Solution(object):
    def pairSum(self, head):
        # 1. Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Calculate the maximum twin sum
        max_sum = 0
        left, right = head, prev
        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum
