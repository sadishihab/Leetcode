class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        return root
    return root

# Return the minimum value node of the BST.
def min_value_node(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = min_value_node(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root


# Inorder traversal (prints tree in sorted order)
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Build a BST
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("Initial tree (inorder):", inorder_traversal(root))

# Remove some nodes
root = remove(root, 20)  # remove leaf
print("After removing 20:", inorder_traversal(root))

root = remove(root, 30)  # remove node with one child
print("After removing 30:", inorder_traversal(root))

root = remove(root, 50)  # remove node with two children
print("After removing 50:", inorder_traversal(root))
