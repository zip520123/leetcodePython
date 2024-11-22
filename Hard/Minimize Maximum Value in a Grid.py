# Minimize Maximum Value in a Grid
# O(m*n log m*n), O(m*n)
def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])

    row_arr = [1] * rows
    col_arr = [1] * cols
    arr = []
    for row in range(rows):
        for col in range(cols):
            arr.append((grid[row][col], row, col))
    arr.sort()

    for n, row, col in arr:
        val = max(row_arr[row], col_arr[col])
        grid[row][col] = val
        row_arr[row] = val + 1 
        col_arr[col] = val + 1
    return grid