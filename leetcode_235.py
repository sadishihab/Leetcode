# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            # Case 1: Both nodes are smaller → go left
            if root.val > p.val and root.val > q.val:
                root = root.left

            # Case 2: Both nodes are larger → go right
            elif root.val < p.val and root.val < q.val:
                root = root.right

            # Case 3: Split point found → current root is LCA
            else:
                return root

