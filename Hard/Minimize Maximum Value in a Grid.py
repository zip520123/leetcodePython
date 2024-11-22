# Minimize Maximum Value in a Grid
# O(m*n log m*n), O(m*n)
def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    row, col = len(grid), len(grid[0])

    nums = []

    rows = [1 for i in range(row)]
    cols = [1 for i in range(col)]

    for i in range(row):
        for j in range(col):
            nums.append((grid[i][j], i, j))

    nums.sort()
    for tup in nums:
        _, i, j = tup

        val = max(rows[i], cols[j])
        grid[i][j] = val

        rows[i], cols[j] = val + 1, val + 1
    return grid