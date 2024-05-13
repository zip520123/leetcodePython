# Score After Flipping Matrix
# O(n), O(1)
def matrixScore(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        if grid[row][0] == 0:
            for col in range(cols):
                grid[row][col] = 1 - grid[row][col]
    for col in range(cols):
        ones, zeros = 0, 0
        for row in range(rows):
            if grid[row][col] == 0:
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            for row in range(rows):
                grid[row][col] = 1 - grid[row][col]
    res = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                res += 2 ** (cols - col - 1)
    
    return res 