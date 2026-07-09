# Triangle
# O(n^2), O(1)
def minimumTotal(self, triangle: List[List[int]]) -> int:
    rows = len(triangle)
    for row in range(1, rows):
        for col in range(row+1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif col == row:
                triangle[row][col] += triangle[row-1][col-1]
            else:
                triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])
    return min(triangle[rows-1])