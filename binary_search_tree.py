class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if not root:
        return False
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True

    # -----------------------
    # Build a sample BST
    #
    #        5
    #       / \
    #      3   8
    #     / \    \
    #    2   4    9
    # -----------------------

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(9)

# Test searches
print(search(root, 4))   # True  (exists)
print(search(root, 9))   # True  (exists)
print(search(root, 7))   # False (not in tree)
print(search(root, 10))  # False (not in tree)