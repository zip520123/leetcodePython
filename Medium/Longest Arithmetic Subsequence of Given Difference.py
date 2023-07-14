# Longest Arithmetic Subsequence of Given Difference
# O(n), O(n)
def longestSubsequence(self, arr: List[int], difference: int) -> int:
    dp = defaultdict(int)
    res = 0
    for n in arr:
        dp[n] = dp[n-difference] + 1
        res = max(res, dp[n])
    return res