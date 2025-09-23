# Definition of a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder Traversal: Left → Root → Right
def inorder(root):
    if not root:
        return                                                  # Base case: stop if node is None
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Preorder Traversal: Root → Left → Right
def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

# Postorder Traversal: Left → Right → Root
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

# Reverse inorder Traversal for getting the largest value first in a BST: Right → Root → Left
def reverse_inorder(root):
    if not root:
        return                                                  # Base case: stop if node is None
    reverse_inorder(root.right)
    print(root.val, end=" ")
    reverse_inorder(root.left)


root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)



# Test traversals
print("Inorder Traversal: ", end="")
inorder(root)
print("\nPreorder Traversal: ", end="")
preorder(root)
print("\nPostorder Traversal: ", end="")
postorder(root)
print("\nreverse inorder Traversal: ", end="")
reverse_inorder(root)