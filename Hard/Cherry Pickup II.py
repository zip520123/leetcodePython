# Cherry Pickup II
# O(rows*cols*cols), O(rows*cols*cols) 
def cherryPickup(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [[-1]*cols for _ in range(cols) ] for _ in range(rows)]

    def dfs(row: int, col1: int, col2: int) -> int:
        if col1 < 0 or col1 == cols or col2 < 0 or col2 == cols: return 0
        if dp[row][col1][col2] != -1: return dp[row][col1][col2]
        res = grid[row][col1] + grid[row][col2]
        if col1 == col2:
            res -= grid[row][col1]
        
        if row == rows-1:
            dp[row][col1][col2] = res
            return res
        maxNextRow = 0
        for a in range(col1-1, col1+2):
            for b in range(col2-1, col2+2):
                maxNextRow = max(maxNextRow, dfs(row+1, a, b))
        res += maxNextRow
        dp[row][col1][col2] = res
        return res
    return dfs(0, 0, cols-1)

# O(rows*cols*cols), O(rows*cols*cols)
def cherryPickup(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [[-1]*cols for _ in range(cols) ] for _ in range(rows)]
    for a in range(cols):
        for b in range(cols):
            dp[rows-1][a][b] = grid[rows-1][a] + grid[rows-1][b]
            if a == b: 
                dp[rows-1][a][b] -= grid[rows-1][a]
    for row in range(rows-2, -1, -1):
        for col1 in range(cols):
            for col2 in range(cols):
                res = grid[row][col1] + grid[row][col2]
                if col1 == col2:
                    res -= grid[row][col1]
                curr = 0
                for a in range(col1-1, col1+2):
                    for b in range(col2-1, col2+2):
                        if 0 <= a < cols and 0 <= b < cols: 
                            curr = max(curr, dp[row+1][a][b])
                dp[row][col1][col2] = res + curr
    return dp[0][0][cols-1]