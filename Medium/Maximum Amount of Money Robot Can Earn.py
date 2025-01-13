# Maximum Amount of Money Robot Can Earn
# O(n*m), O(n*m)
def maximumAmount(self, coins: List[List[int]]) -> int:
    dp = {}
    rows, cols = len(coins), len(coins[0])
    dp[(0,0,0)] = coins[0][0]
    dp[(0,0,1)] = 0
    dp[(0,0,2)] = 0

    for i in range(1, cols):
        dp[(0, i, 0)] = dp[(0, i - 1, 0)] + coins[0][i]
        dp[(0, i, 1)] = max(dp[(0, i - 1, 1)] + coins[0][i], dp[(0, i - 1, 0)])
        dp[(0, i, 2)] = max(dp[(0, i - 1, 2)] + coins[0][i], dp[(0, i - 1, 1)])

    for i in range(1, rows):
        dp[(i, 0, 0)] = dp[(i-1, 0, 0)] + coins[i][0]
        dp[(i, 0, 1)] = max(dp[(i-1, 0, 1)] + coins[i][0], dp[(i-1, 0, 0)])
        dp[(i, 0, 2)] = max(dp[(i-1, 0, 2)] + coins[i][0], dp[(i-1, 0, 1)])

    for row in range(1, rows):
        for col in range(1, cols):
            coin = coins[row][col]
            dp[(row, col, 0)] = max(dp[(row-1, col, 0)], dp[((row, col-1, 0))]) + coin
            dp[(row, col, 1)] = max(max(dp[(row-1, col, 1)], dp[((row, col-1, 1))]) + coin, dp[(row-1, col, 0)], dp[(row, col-1, 0)])
            dp[(row, col, 2)] = max(max(dp[(row-1, col, 2)], dp[((row, col-1, 2))]) + coin, dp[(row-1, col, 1)], dp[(row, col-1, 1)])

    return max(dp[(rows-1, cols-1, 0)], dp[(rows-1, cols-1, 1)], dp[(rows-1, cols-1, 2)])
