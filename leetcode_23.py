# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge_sort(lists, 0, len(lists) - 1)

    def merge_sort(self, lists, left, right):
        # Base case: single list
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        # Divide into two halves
        l1 = self.merge_sort(lists, left, mid)
        l2 = self.merge_sort(lists, mid + 1, right)
        # Conquer: merge two sorted lists
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # Attach remaining nodes
        curr.next = l1 if l1 else l2
        return dummy.next
