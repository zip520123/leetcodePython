# Best Sightseeing Pair
# O(n), O(n)
def maxScoreSightseeingPair(self, values: List[int]) -> int:
    dp = [0] * len(values)
    dp[0] = values[0]
    for i in range(1, len(values)):
        dp[i] = max(dp[i-1], values[i] + i)
    res = 0
    for i in range(1, len(values)):
        res = max(res, dp[i-1] + values[i] - i )
    return res