# Find Valid Matrix Given Row and Column Sums
# O(n), O(1)
def restoreMatrix(self, rowSum, colSum):
    rows, cols = len(rowSum), len(colSum)
    res = [ [0] * cols for _ in range(rows) ]
    for row in range(rows):
        for col in range(cols):
            mn = min(rowSum[row], colSum[col])
            res[row][col] = mn
            rowSum[row] -= mn
            colSum[col] -= mn
    return res