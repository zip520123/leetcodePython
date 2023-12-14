# Difference Between Ones and Zeros in Row and Column
# O(n), O(n)
def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    rowsMap = {}
    for i in range(rows):
        row = grid[i]
        rowsMap[i] = sum(row)
    colsMap = {}
    for col in range(cols):
        curr = 0
        for row in range(rows):
            curr += grid[row][col]
        colsMap[col] = curr
    res = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            onesRow = rowsMap[row]
            zeroRow = rows-onesRow
            onesCol = colsMap[col]
            zeroCol = cols-onesCol
            res[row][col] = onesRow + onesCol - zeroRow - zeroCol
    return res