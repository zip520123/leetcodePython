# Transpose Matrix
# O(n), O(n)
def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    rows, cols = len(matrix), len(matrix[0])
    newRows, newCols = cols, rows
    res = [[0]*newCols for _ in range(newRows)]
    for row in range(rows):
        for col in range(cols):
            res[col][row] = matrix[row][col]
    return res