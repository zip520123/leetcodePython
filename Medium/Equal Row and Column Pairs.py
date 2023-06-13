# Equal Row and Column Pairs
# O(rows*cols), O(row+col)
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