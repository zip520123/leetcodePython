# Equal Row and Column Pairs
# O(rows*cols*rows), O(row+col)
def equalPairs(self, grid: List[List[int]]) -> int:
    res = 0
    rows = len(grid); cols = len(grid[0])
    for i in range(rows):
        arr1 = grid[i]
        for col in range(cols):
            arr2 = []
            for j in range(rows):
                arr2.append(grid[j][col])
            if arr1 == arr2:
                res += 1
    return res

# O(rows*cols*rows), O(1)
def equalPairs(self, grid: List[List[int]]) -> int:
    res = 0
    n = len(grid)
    for i in range(n):
        arr1 = grid[i]
        for col in range(n):
            for row in range(n):
                n2 = grid[row][col]
                n1 = arr1[row]
                if n1 != n2:
                    break
            else:
                res += 1
    return res

# O(rows*cols), O(cols)
def equalPairs(self, grid: List[List[int]]) -> int:
    res = 0
    n = len(grid)
    colsArr = collections.defaultdict(int)
    for col in range(n):
        arr = []
        for row in range(n):
            arr.append(grid[row][col])
        colsArr[tuple(arr)] += 1

    for i in range(n):
        arr = grid[i]
        if tuple(arr) in colsArr:
            res += colsArr[tuple(arr)]
                
    return res