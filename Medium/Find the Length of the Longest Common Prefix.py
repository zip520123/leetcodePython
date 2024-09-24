# Find the Length of the Longest Common Prefix
# O(n), O(n)
class Trie:
    def __init__(self):
        self.memo = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Trie()
        for n in arr1:
            curr = root
            s = str(n)
            for char in s:
                if char not in curr.memo:
                    curr.memo[char] = Trie()
                curr = curr.memo[char]
            curr.isEnd = True
        
        res = 0
        for n in arr2:
            s = str(n)
            curr = root
            for i in range(len(s)):
                if s[i] in curr.memo:
                    curr = curr.memo[s[i]]
                    res = max(res, i+1)
                else:
                    break
        return res