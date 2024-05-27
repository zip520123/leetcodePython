# Palindrome Partitioning
# O(n!), O(n)
def partition(self, s: str) -> List[List[str]]:
    def dfs(index: int, path: List[str]) -> List[List[str]]:
        if index == len(s):
            return [path]
        res = []
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                res += dfs(i+1, path + [s[index:i+1]])
        return res
    return dfs(0,[])

def partition(self, s: str) -> List[List[str]]:
    res = []
    def dfs(index: int, path: List[str]):
        if index == len(s):
            res.append(path)
            return
        
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                dfs(i+1, path + [s[index:i+1]])
    dfs(0,[])
    return res

def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True