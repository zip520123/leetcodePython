# Find the Safest Path in a Grid
# O(n log n), O(n)
def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    score = [[math.inf]*cols for _ in range(rows)]
    if grid[0][0] or grid[rows-1][cols-1]:
        return 0
    queue = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                score[row][col] = 0
                queue.append((row, col, 0))
    while queue:
        temp = queue
        queue = []
        for row, col, curr_score in temp:
            for d_row, d_col in [(0,1),(0,-1),(1,0),(-1,0)]:
                nextRow, nextCol = row+d_row, col+d_col
                if 0 <= nextCol < cols and 0 <= nextRow < rows:
                    if score[nextRow][nextCol] > curr_score + 1:
                        score[nextRow][nextCol] = curr_score + 1
                        queue.append((nextRow, nextCol, curr_score + 1))
    
    heap = [(-score[0][0], -score[0][0],0,0)]
    seen = set()
    seen.add((0,0))
    while heap:
        currScore, path, row, col = heapq.heappop(heap)
        currScore = -currScore
        path = -path
        if row == rows-1 and col == cols-1:
            return path
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nextRow, nextCol = row+dy, col+dx
            if 0 <= nextCol < cols and 0 <= nextRow < rows:
                if (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    nextPath = min(path, score[nextRow][nextCol])
                    heapq.heappush(heap, (-score[nextRow][nextCol], -nextPath, nextRow, nextCol))

    return 1