# Maximum Matrix Sum
# O(n), O(1)
def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    res = 0
    max_nagative = -math.inf
    min_postive = math.inf
    nagative_count = 0
    has_zero = False
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] < 0:
                res -= matrix[row][col]
                max_nagative = max(max_nagative, matrix[row][col])
                nagative_count += 1
            elif matrix[row][col] == 0:
                has_zero = True
            else:
                res += matrix[row][col]
                min_postive = min(min_postive, matrix[row][col])
    
    if nagative_count % 2 == 1 and has_zero == False:
        res -= min(abs(max_nagative), min_postive) * 2
    return res