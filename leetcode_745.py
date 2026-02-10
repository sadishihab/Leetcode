class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class WordFilter:
    def __init__(self, words):
        self.root = TrieNode()

        for i, word in enumerate(words):
            long_word = "#" + word
            for j in range(len(word) + 1):
                curr = self.root
                curr.index = i
                for c in word[j:] + long_word:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                    curr.index = i

    def f(self, pref, suff):
        curr = self.root
        search = suff + "#" + pref
        for c in search:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.index
