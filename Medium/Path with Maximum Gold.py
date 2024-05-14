# Path with Maximum Gold
# O(n^2), O(n)
def getMaximumGold(self, grid: List[List[int]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(row: int, col: int) -> int:
        if not(0 <= row < rows and 0 <= col < cols and grid[row][col] > 0): 
            return 0
        temp = grid[row][col]
        grid[row][col] = 0
        next = 0
        next = max(next, dfs(row, col+1))
        next = max(next, dfs(row, col-1))
        next = max(next, dfs(row+1, col))
        next = max(next, dfs(row-1, col))
        grid[row][col] = temp
        return temp + next
    
    for row in range(rows):
        for col in range(cols):
            res = max(res, dfs(row, col))
    return res

# O(n^2), O(n)
def getMaximumGold(self, grid: List[List[int]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(path: int, row: int, col: int):
        nonlocal res
        if not(0 <= row < rows and 0 <= col < cols and grid[row][col] > 0): 
            res = max(res, path)
            return
        temp = grid[row][col]
        grid[row][col] = 0
        
        dfs(path+temp, row, col+1)
        dfs(path+temp, row, col-1)
        dfs(path+temp, row+1, col)
        dfs(path+temp, row-1, col)
        grid[row][col] = temp
        
    for row in range(rows):
        for col in range(cols):
            dfs(0, row, col)
    return res