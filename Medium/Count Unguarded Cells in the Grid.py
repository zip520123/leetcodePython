# Count Unguarded Cells in the Grid
# O(m*n), O(m*n)
def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    grid = [[0] * n for _ in range(m)]
    for x,y in guards:
        grid[x][y] = 1
    for x,y in walls:
        grid[x][y] = 1

    def check_right(x, y):
        if not (0 <= x < m and 0 <= y < n and grid[x][y] != 1):
            return 
        grid[x][y] = 2
        check_right(x, y+1)
    
    def check_left(x, y):
        if not (0 <= x < m and 0 <= y < n and grid[x][y] != 1):
            return 
        grid[x][y] = 2
        check_left(x, y-1)
    
    def check_top(x, y):
        if not (0 <= x < m and 0 <= y < n and grid[x][y] != 1):
            return 
        grid[x][y] = 2
        check_top(x-1, y)
    
    def check_bottom(x, y):
        if not (0 <= x < m and 0 <= y < n and grid[x][y] != 1):
            return 
        grid[x][y] = 2
        check_bottom(x+1, y)
    
    for x,y in guards:
        check_right(x, y+1)
        check_left(x, y-1)
        check_top(x-1, y)
        check_bottom(x+1, y)
    
    res = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                res += 1

    return res