# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()

                # if this is the last node in the level → add to result
                if i == level_size - 1:
                    result.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return result
