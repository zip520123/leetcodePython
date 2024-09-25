# Sum of Prefix Scores of Strings
# O(n), O(n)
class Trie:
    def __init__(self):
        self.memo = {}
        self.n = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.memo:
                    curr.memo[char] = Trie()
                curr = curr.memo[char]
                curr.n += 1
        res = []
        for word in words:
            curr = root
            count = 0
            for char in word:
                if char not in curr.memo:
                    break
                curr = curr.memo[char]
                count += curr.n
            res.append(count)
        return res