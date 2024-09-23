# Extra Characters in a String
# O(n^2), O(n)
class Trie:
    def __init__(self):
        self.map = {}
        self.n = None
class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.map:
                    curr.map[char] = Trie()
                curr = curr.map[char]
            curr.n = len(word)
        
        @cache
        def dfs(index: int, rest: int) -> int:
            if index == len(s): return rest
            res = rest
            for i in range(index, len(s)):
                curr = root
                j = i
                
                while j < len(s) and s[j] in curr.map: 
                    curr = curr.map[s[j]]
                    j += 1
                    if curr.n is not None:
                        res = min(res, dfs(j, rest-curr.n))
            return res
        return dfs(0, len(s))
    

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.memo:
                    curr.memo[char] = Trie()
                curr = curr.memo[char]
            curr.isEnd = True
        
        @cache
        def dfs(index: int, rest: int) -> int:
            if index == len(s):
                return rest
            res = rest
            for i in range(index, len(s)):
                curr = root
                j = i
                while j<len(s) and s[j] in curr.memo: 
                    curr = curr.memo[s[j]]
                    j += 1
                    if curr.isEnd:
                        res = min(res, dfs(j, rest-(j-i)))
            return res

        return dfs(0, len(s))