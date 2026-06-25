#  Design Add and Search Words Data Structure
# O(n), O(n)
class Trie:
    def __init__(self):
        self.memo = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None: #O(L), L is the length of the word
        curr = self.root
        for char in word:
            if char not in curr.memo:
                curr.memo[char] = Trie()
            curr = curr.memo[char]
        curr.isEnd = True

    def searchNode(self, word, curr) -> bool: #O(26^d * L), L is the length of the word, d is dots
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                res = False
                for val in curr.memo.values():
                    res = res or self.searchNode(word[i+1:], val)
                return res
            else:
                if char not in curr.memo:
                    return False
                curr = curr.memo[char]
        return curr.isEnd

    def search(self, word: str) -> bool:
        return self.searchNode(word, self.root)
    

# DFS
    def searchNode(self, word, curr) -> bool:
        if not word:
            return curr.isEnd
        char = word[0]
        if char == ".":
            for val in curr.memo.values():
                if self.searchNode(word[1:], val):
                    return True
            return False
        if char not in curr.memo:
            return False
        
        return self.searchNode(word[1:], curr.memo[char])
