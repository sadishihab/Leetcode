from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level_nodes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_nodes.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level_nodes)                          #adding current level nodes to the result
        return result

