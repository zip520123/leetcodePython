# Perfect Squares
# O(n log n), O(n)
def numSquares(self, n: int) -> int:
    dp = [num for num in range(n+1)]
    for i in range(n+1):
        j = 2
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[n]