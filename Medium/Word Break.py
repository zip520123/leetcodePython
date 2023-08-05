# Word Break
# O(s.len ^ 2 + wordDict.len), O(s.len + wordDict.len)
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie()
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Trie()
                curr = curr.children[char]
            curr.isEnd = True
        
        memo = {}
        def dfs(s: str) -> bool:
            if s == "": return True
            if s in memo: return memo[s]
            res = False
            curr = root
            for i in range(len(s)):
                char = s[i]
                if char in curr.children:
                    curr = curr.children[char]
                    if curr.isEnd:
                        res = res or dfs(s[i+1:])
                else:
                    break
            memo[s] = res
            return memo[s]
        
        return dfs(s)
    
# O(s.len * wordDict.len), O(s.len)
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    @cache
    def dfs(i: int) -> bool:
        if i < 0: return True

        for word in wordDict:
            if s[i - len(word) + 1 : i+1] == word and dfs(i-len(word)):
                return True
        return False

    return dfs(len(s)-1)