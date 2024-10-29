# Maximum Number of Moves in a Grid
# O(n), O(n)
def maxMoves(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [0]*cols for _ in range(rows) ]
    for col in range(1, cols):
        for row in range(rows):
            if grid[row][col] > grid[row][col-1]:
                dp[row][col] = max(dp[row][col], dp[row][col-1] + 1)
            if row - 1 >= 0 and grid[row][col] > grid[row-1][col-1]:
                dp[row][col] = max(dp[row][col], dp[row-1][col-1] + 1)
            if row + 1 < rows and grid[row][col] > grid[row+1][col-1]:
                dp[row][col] = max(dp[row][col], dp[row+1][col-1] + 1)
    
    res = 0
    for row in range(rows):
        for col in range(cols):
            if dp[row][col] == col:
                res = max(res, dp[row][col])
    return res