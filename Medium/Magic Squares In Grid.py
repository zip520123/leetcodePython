# Magic Squares In Grid
# O(n), O(1)
def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    nums_set = set([ i for i in range(1,10)])
    res = 0
    for i in range(rows-2):
        for j in range(cols-2):
            curr_set = set()
            for row in range(i,i+3):
                for col in range(j, j+3):
                    curr_set.add(grid[row][col])
            if nums_set != curr_set:
                continue
            col_count = 0
            for col in range(j, j+3):
                col_count += grid[i][col]
            if col_count != 15:
                continue
            row_count = 0
            for row in range(i, i+3):
                row_count += grid[row][j]
            if row_count != 15:
                continue
            diag_count = 0
            for d in range(3):
                diag_count += grid[i+d][j+d]
            if diag_count != 15:
                continue
            anti_diag_count = 0
            for dx, dy in [(0,2), (1,1), (2,0)]:
                anti_diag_count += grid[i+dx][j+dy]
            if anti_diag_count != 15:
                continue
            res += 1
    return res