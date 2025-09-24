# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root_val = preorder[0]                                           # root is always the first in preorder
        root = TreeNode(root_val)                                        # make the root node

        mid = inorder.index(root_val)                                    # find root in inorder

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])     # left subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])   # right subtree

        return root

