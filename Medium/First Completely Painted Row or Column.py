# First Completely Painted Row or Column
# O(n), O(n)
def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
    rows, cols = len(mat), len(mat[0])
    rows_dp = [cols] * rows
    cols_dp = [rows] * cols
    num_to_row_col = {}
    for row in range(rows):
        for col in range(cols): 
            n = mat[row][col]
            num_to_row_col[n] = (row, col)
    
    for i in range(len(arr)):
        n = arr[i]
        row, col = num_to_row_col[n]
        rows_dp[row] -= 1
        if rows_dp[row] == 0:
            return i
        cols_dp[col] -= 1
        if cols_dp[col] == 0:
            return i
    return 0