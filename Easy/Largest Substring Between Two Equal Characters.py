# Largest Substring Between Two Equal Characters
# O(n^2), O(1)
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    res = -1
    n = len(s)
    for i in range(n-1):
        for j in range(i+1,n):
            if s[i] == s[j]:
                res = max(res, j-(i+1))
    return res

# O(n), O(1)
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    res = -1
    n = len(s)
    memo = {}
    for i in range(n):
        memo[s[i]] = i
    for i in range(n):
        res = max(res, memo[s[i]]-(i+1))
    return res