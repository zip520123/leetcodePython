# Word Break II
# O(2^n), O(n)
class Trie:
    def __init__(self):
        self.dic = {}
        self.isEnd = False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Trie()
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.dic:
                    curr.dic[char] = Trie()
                curr = curr.dic[char]
            curr.isEnd = True

        def dfs(path: List[str], index: int) -> List[str]:
            if index == len(s):
                return [" ".join(path)]
            res = []
            for i in range(index, len(s)):
                word = s[index:i+1]
                if self.find(word, root):
                    res += dfs(path + [s[index:i+1]], i+1)
            return res

        return dfs([], 0)

    def find(self, word: str, root: Trie) -> bool:
        curr = root
        for char in word:
            if char not in curr.dic:
                return False
            curr = curr.dic[char]
        return curr.isEnd