from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("Level:", level, "→", end=" ")
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()
        level += 1


# -------------------------
# Build example tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
# -------------------------

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Run BFS
print("BFS Level Order Traversal:")
bfs(root)