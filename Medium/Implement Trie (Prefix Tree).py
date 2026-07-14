# Implement Trie (Prefix Tree)
# O(n) time complexity for insert, search, and startsWith operations, where n is the length of the word or prefix.
class TrieNode:
    def __init__(self):
        self.memo = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in  curr.memo:
                curr.memo[char] = TrieNode()
            curr = curr.memo[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.memo:
                return False
            curr = curr.memo[char]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.memo:
                return False
            curr = curr.memo[char]
        return True