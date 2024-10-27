# Count Square Submatrices with All Ones
# O(n), O(n)
def countSquares(self, matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col]:
                matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])
    return sum(sum(row) for row in matrix)