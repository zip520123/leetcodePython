# Number of Submatrices That Sum to Target
# O(m^2*n^2), O(mn), TLE
def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0]*cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            dp[row][col] = matrix[row][col]
            if row > 0:
                dp[row][col] += dp[row-1][col]
            if col > 0:
                dp[row][col] += dp[row][col-1]
            if row > 0 and col > 0:
                dp[row][col] -= dp[row-1][col-1]
    res = 0

    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    top = dp[r1-1][c2] if r1 > 0 else 0
                    left = dp[r2][c1-1] if c1 > 0 else 0
                    top_left = dp[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
                    curr_sum = dp[r2][c2] - top - left + top_left

                    if curr_sum == target:
                        res += 1

    return res