# Number of Islands
# O(n), O(n)
def numIslands(self, grid: List[List[str]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(row, col):
        if not (0 <= row < rows and 0<= col < cols): return
        nonlocal grid
        if grid[row][col] == "0": return
        grid[row][col] = "0"
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            dfs(row+dx,col+dy)
        
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                res += 1
                dfs(row, col)
    return res