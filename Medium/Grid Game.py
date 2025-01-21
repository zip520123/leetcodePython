# Grid Game
# O(n), O(1)
def gridGame(self, grid: List[List[int]]) -> int:
    row0_sum = sum(grid[0])
    row1_sum = 0
    res = math.inf
    for i in range(len(grid[0])):
        row0_sum -= grid[0][i]
        res = min(res, max(row0_sum, row1_sum))
        row1_sum += grid[1][i]
    return res