# Maximum Score After Splitting a String
# O(n), O(1)
def maxScore(self, s: str) -> int:
    n = len(s)
    ones = 0
    for char in s:
        if char == "1":
            ones += 1
    res = 0
    zeros = 0
    for i in range(0,n-1):
        char = s[i]
        if char == "0": zeros += 1
        if char == "1": ones -= 1
        res = max(res, zeros + ones)
    return res

# O(n), O(1)
def maxScore(self, s: str) -> int:
    res = 0
    zeros, ones = 0, 0

    if s[0] == "0":
        zeros += 1
    
    for i in range(1, len(s)):
        if s[i] == "1":
            ones += 1

    for i in range(1, len(s)):
        res = max(res, zeros + ones)
        if s[i] == "0":
            zeros += 1
        else:
            ones -= 1
    return res