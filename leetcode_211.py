class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return node.word

            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(i + 1, node.children[c])

        return dfs(0, self.trie.root)
