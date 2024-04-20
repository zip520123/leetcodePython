# Island Perimeter
# O(n), O(1)
def islandPerimeter(self, grid: List[List[int]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                if row - 1 < 0: 
                    res += 1
                if row + 1 == rows: 
                    res += 1
                if col - 1 < 0: 
                    res += 1
                if col + 1 == cols: 
                    res += 1
                if row - 1 >= 0 and grid[row-1][col] == 0:
                    res += 1
                if row + 1 < rows and grid[row+1][col] == 0:
                    res += 1
                if col - 1 >= 0 and grid[row][col-1] == 0:
                    res += 1
                if col + 1 < cols and grid[row][col+1] == 0:
                    res += 1
    return res