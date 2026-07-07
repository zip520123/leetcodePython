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

# O(m*n), O(1)
def setZeroes(self, matrix: List[List[int]]) -> None:
    first_row_has_zero = False
    first_col_has_zero = False
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        if matrix[row][0] == 0:
            first_col_has_zero = True
    for col in range(cols):
        if matrix[0][col] == 0:
            first_row_has_zero = True
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
    for row in range(1, rows):
        if matrix[row][0] == 0:
            for col in range(1, cols):
                matrix[row][col] = 0
    
    for col in range(1, cols):
        if matrix[0][col] == 0:
            for row in range(1, rows):
                matrix[row][col] = 0
    
    if first_col_has_zero:
        for row in range(rows):
            matrix[row][0] = 0
    
    if first_row_has_zero:
        for col in range(cols):
            matrix[0][col] = 0
