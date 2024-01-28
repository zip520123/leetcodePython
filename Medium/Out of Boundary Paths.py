# Out of Boundary Paths
# O(m*n*maxMove), O(m*n*maxMove)
@cache
def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n: 
        return 1
    if maxMove == 0:
        return 0
    
    res = 0
    res += self.findPaths(m,n,maxMove-1,startRow+1,startColumn)
    res += self.findPaths(m,n,maxMove-1,startRow-1,startColumn)
    res += self.findPaths(m,n,maxMove-1,startRow,startColumn+1)
    res += self.findPaths(m,n,maxMove-1,startRow,startColumn-1)
    return res % (10 ** 9 + 7)


def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    memo = {}

    def dfs(maxMove, row, col):
        if (maxMove, row, col) in memo:
            return memo[(maxMove, row, col)]
        if row < 0 or row == m or col < 0 or col == n: 
            return 1
        if maxMove == 0:
            return 0
        
        res = 0
        res += dfs(maxMove-1,row+1,col)
        res += dfs(maxMove-1,row-1,col)
        res += dfs(maxMove-1,row,col+1)
        res += dfs(maxMove-1,row,col-1)
        memo[(maxMove, row, col)] = res % (10 ** 9 + 7)
        return memo[(maxMove, row, col)]
    return dfs(maxMove, startRow, startColumn)