class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store word directly


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            nxt = node.children[char]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = char  # backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return res
