# Longest Ideal Subsequence
# O(n^2), O(n) TLE
def longestIdealString(self, s: str, k: int) -> int:
    n = len(s)
    arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if abs(ord(s[i])-ord(s[j])) <= k:
                arr[i] = max(arr[i], arr[j]+1)
    return max(arr)

# O(n*(2k+1)), O(1)
def longestIdealString(self, s: str, k: int) -> int:
    l = [0] * 128
    for c in s:
        i = ord(c)
        l[i] = max(l[i - k : i + k + 1]) + 1
    return max(l)