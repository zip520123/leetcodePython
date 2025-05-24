# Set Matrix Zeroes
# O(m*n), O(m+n)
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows, cols = len(matrix), len(matrix[0])
    row_arr, col_arr = set(), set()
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                row_arr.add(row)
                col_arr.add(col)
    
    for row in range(rows):
        for col in range(cols):
            if row in row_arr or col in col_arr:
                matrix[row][col] = 0