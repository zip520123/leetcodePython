# Pascal's Triangle
# O(n), O(1)
def generate(self, numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        res.append([1 for _ in range(i+1)])
        for j in range(1,i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res