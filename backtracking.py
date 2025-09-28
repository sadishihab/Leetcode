class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# backtracking only returning true or false if the tree has a path
def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False

# backtracking and returning the path
def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False

# -------------------------
# Build example tree:
#         1
#        / \
#       2   3
#        \
#         0
# -------------------------

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(0)

# Test canReachLeaf
print("Can reach leaf without 0?", canReachLeaf(root))  # Expected: True (path 1 → 3)

# Test leafPath
path = []
found = leafPath(root, path)
print("Path to leaf without 0:", path if found else "No valid path")  # Expected: [1, 3]
