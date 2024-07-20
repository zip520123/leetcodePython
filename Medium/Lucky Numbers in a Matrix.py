# Lucky Numbers in a Matrix
# O(n), O(n)
def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])
    min_arr = []
    for row in range(rows):
        curr = math.inf
        
        for col in range(cols):
            if matrix[row][col] < curr:
                curr = matrix[row][col]
        min_arr.append(curr)
    max_arr = []
    for col in range(cols):
        curr = -math.inf
        for row in range(rows):
            if matrix[row][col] > curr:
                curr = matrix[row][col]
        max_arr.append(curr)
    return set(min_arr) & set(max_arr)