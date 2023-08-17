# 01 Matrix
# O(n), O(n)
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    rows = len(mat); cols = len(mat[0])
    dp = [[0]*cols for _ in range(rows)]
    queue = []
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0:
                queue.append([row,col])
            else:
                dp[row][col] = -1
                
    while len(queue) > 0:
        temp = queue
        queue = []
        for row,col in temp:
            val = dp[row][col]
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nextRow = row+dy
                nextCol = col+dx
                if nextRow >= 0 and nextRow < rows and nextCol >= 0 and nextCol < cols and dp[nextRow][nextCol] == -1:
                    dp[nextRow][nextCol] = val + 1
                    queue.append([nextRow, nextCol])
    return dp