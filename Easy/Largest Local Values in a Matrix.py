# Largest Local Values in a Matrix
# O(n), O(n)
def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    res = []
    rows, cols = len(grid), len(grid[0])
    for row in range(rows-2):
        currRow = []
        for col in range(cols-2):
            curr = 0
            for i in range(row, row+3):
                for j in range(col, col+3):
                    curr = max(curr, grid[i][j])
            currRow.append(curr)
        res.append(currRow)
    return res