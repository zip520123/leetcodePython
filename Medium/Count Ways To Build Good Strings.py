# Count Ways To Build Good Strings
# O(high) time complexity, O(high) space complexity
def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    dp = [0] * (high + 1)
    dp[0] = 1
    for end in range(1, high+1):
        if end >= zero:
            dp[end] += dp[end-zero]
        if end >= one:
            dp[end] += dp[end-one]
        dp[end] %= (10 ** 9 + 7)
    
    return sum(dp[low: high+1]) % (10**9+7)

# O(high), O(high)
def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    dp = [-1] * (high + 1)
    dp[0] = 1

    def dfs(curr_count: int) -> int:
        if dp[curr_count] != -1:
            return dp[curr_count]
        res = 0
        if curr_count - zero >= 0:
            res += dfs(curr_count - zero)
        if curr_count - one >= 0:
            res += dfs(curr_count - one)
        res %= (10 ** 9 + 7)
        dp[curr_count] = res
        return res
    
    return sum( dfs(end) for end in range(low, high + 1) ) % (10 ** 9 + 7)