# Unique Paths II
# O(n), O(n)
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * cols for _ in range(rows)]
    
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    for row in range(1,rows):
        if obstacleGrid[row][0] == 0: dp[row][0] = dp[row-1][0]

    for col in range(1,cols):
        if obstacleGrid[0][col] == 0: dp[0][col] = dp[0][col-1]
    
    for row in range(1,rows):
        for col in range(1,cols):
            if obstacleGrid[row][col] == 0:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
    
    return dp[rows-1][cols-1]