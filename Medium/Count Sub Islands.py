# Count Sub Islands
# O(row*col), O(row*col)
def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    rows, cols = len(grid1), len(grid1[0])
    res = 0

    def dfs(row, col) -> bool:
        nonlocal grid2
        if grid2[row][col] == 0: return False
        
        curr = grid1[row][col] == 1
        grid2[row][col] = 0
        
        if row+1 < rows and grid2[row+1][col] == 1:
            curr &= dfs(row+1,col)
        
        if 0 <= row-1 and grid2[row-1][col] == 1:
            curr &= dfs(row-1,col)

        if col+1 < cols and grid2[row][col+1] == 1:
            curr &= dfs(row, col+1)  

        if 0 <= col-1  and grid2[row][col-1] == 1:
            curr &= dfs(row,col-1)

        return curr

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col):
                res += 1
    return res