# Matrix Diagonal Sum
# O(n) time, O(1) space
def diagonalSum(self, mat: List[List[int]]) -> int:
    res = 0
    n = len(mat)-1
    for i in range(0,len(mat)):
        res += mat[i][i]
        res += mat[i][n-i]
        if i == n-i:
            res -= mat[i][n-i]
    return res
