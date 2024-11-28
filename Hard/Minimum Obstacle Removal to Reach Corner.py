# Minimum Obstacle Removal to Reach Corner
# O(n log n), O(n), Dijkstra 
def minimumObstacles(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [math.inf] * cols for _ in range(rows) ]
    dp[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        obstacles_encounterd, row, col = heapq.heappop(heap)
        for d_row, d_col in [(0,1), (1,0), (-1,0), (0,-1)]:
            next_row, next_col = row+d_row, col+d_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if dp[row][col] + grid[next_row][next_col] < dp[next_row][next_col]:
                    dp[next_row][next_col] = dp[row][col] + grid[next_row][next_col]
                    heapq.heappush(heap, (dp[next_row][next_col], next_row, next_col))
    return dp[rows-1][cols-1]


# O(n), O(n) deque, BFS
def minimumObstacles(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [math.inf] * cols for _ in range(rows) ]
    dp[0][0] = 0
    deque = [(0, 0)]
    while deque:
        row, col = deque.pop(0) 
        for d_row, d_col in [(0,1), (1,0), (-1,0), (0,-1)]:
            next_row, next_col = row+d_row, col+d_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if dp[row][col] + grid[next_row][next_col] < dp[next_row][next_col]:
                    dp[next_row][next_col] = dp[row][col] + grid[next_row][next_col]
                    if grid[next_row][next_col] == 1:
                        deque.append((next_row, next_col))
                    else:
                        deque.insert(0, (next_row, next_col))
                    
    return dp[rows-1][cols-1]