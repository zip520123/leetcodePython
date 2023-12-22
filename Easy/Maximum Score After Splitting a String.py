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