# Minimum Falling Path Sum
# O(n), O(1)
def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    for row in range(1, rows):
        for col in range(cols):
            if col == 0:
                matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col+1])
            elif 0 < col < cols-1:
                matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1], matrix[row-1][col+1])
            else:
                matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1])
    return min(matrix[rows-1])