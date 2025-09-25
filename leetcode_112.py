# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
      if not root:
          return False

      if not root.left and not root.right:
          return targetSum == root.val

      return (self.hasPathSum(root.left, targetSum - root.val) or               #this code and below code are same. Just an elegant style of coding.
              self.hasPathSum(root.right, targetSum - root.val))






      # if self.hasPathSum(root.left, targetSum - root.val):
      #     return True
      # if self.hasPathSum(root.right, targetSum - root.val):
      #     return True
      # return False

