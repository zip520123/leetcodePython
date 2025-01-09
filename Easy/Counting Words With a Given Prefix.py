# Counting Words With a Given Prefix
# O(n), O(n)
class Trie:
    def __init__(self):
        self.freq = 0
        self.memo = {}

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        root = Trie()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.memo:
                    curr.memo[char] = Trie()
                curr = curr.memo[char]
                curr.freq += 1
        curr = root
        for char in pref:
            if char not in curr.memo:
                return 0
            curr = curr.memo[char]
        return curr.freq

# O(n), O(1)
def prefixCount(self, words: List[str], pref: str) -> int:
    res = 0
    for word in words:
        isPref = True
        for i in range(len(pref)):
            if i >= len(word) or word[i] != pref[i]:
                isPref = False
                break
        if isPref:
            res += 1
    return res