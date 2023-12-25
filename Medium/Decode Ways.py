# Decode Ways
# O(n), O(n)
def numDecodings(self, s: str) -> int:
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        if int(s[i]) > 0: dp[i+1] = dp[i]
        if i>0 and 9<int(s[i-1:i+1])<=26: dp[i+1] += dp[i-1]
    return dp[n]
    