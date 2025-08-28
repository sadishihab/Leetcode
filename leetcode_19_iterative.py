# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()                      #initializing dummy to keep track of the first node. classic linked list trick to make the algorithm simpler and cleaner.
        curr = dummy
        while list1 and list2:                  #Loop runs until reach to a empty node
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:                               # Merging the remaining
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next                       # Return the head of merged list.

