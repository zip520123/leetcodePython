# Spiral Matrix III
# O(n), O(1)
def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    res = []
    d = 1
    direct = 0
    curr_row, curr_col = rStart, cStart
    
    if 0 <= curr_row < rows and 0 <= curr_col < cols:
        res.append([curr_row, curr_col])

    while len(res) < rows*cols:
        if direct == 0:
            for _ in range(d):
                curr_col += 1
                if 0 <= curr_row < rows and 0 <= curr_col < cols:
                    res.append([curr_row, curr_col])
            for _ in range(d):
                curr_row += 1
                if 0 <= curr_row < rows and 0 <= curr_col < cols:
                    res.append([curr_row, curr_col])
        else:
            for _ in range(d):
                curr_col -= 1
                if 0 <= curr_row < rows and 0 <= curr_col < cols:
                    res.append([curr_row, curr_col])
            for _ in range(d):
                curr_row -= 1
                if 0 <= curr_row < rows and 0 <= curr_col < cols:
                    res.append([curr_row, curr_col])
        direct = (direct + 1) % 2
        d += 1
    return res