# Equal Row and Column Pairs
# O(rows*cols*n), O(1)
def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)
    rows, cols = n, n
    res = 0
    
    for row in range(rows):
        for col in range(cols):
            same = True
            for i in range(n):
                if grid[row][i] != grid[i][col]:
                    same = False
            if same:
                res += 1                
    return res

# O(rows*cols*n), O(rows*cols)
def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)
    rows, cols = n, n
    res = 0
    row_map = {}
    col_map = {}

    for row in range(rows):
        row_map[row] = grid[row]
    for col in range(cols):
        arr = []
        for row in range(rows):
            arr.append(grid[row][col])
        col_map[col] = arr
    
    for row in range(rows):
        for col in range(cols):
            if row_map[row] == col_map[col]:
                res += 1
    return res

# O(rows*cols), O(rows*cols)
def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)
    rows, cols = n, n
    res = 0
    row_count = Counter(tuple(row) for row in grid)
    for col in range(cols):
        arr = []
        for row in range(rows):
            arr.append(grid[row][col])
        res += row_count[tuple(arr)]
    return res