# Minimum Time to Visit a Cell In a Grid
# O(n^2), O(n), TLE
def minimumTime(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    heap = [(0, 0, 0)]
    while heap:
        steps, row, col = heapq.heappop(heap)
        if row == rows-1 and col == cols -1:
            return steps
        steps += 1
        for d_row, d_col in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_row, next_col = row+d_row, col+d_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if steps >= grid[next_row][next_col]:
                    heapq.heappush(heap, (steps, next_row, next_col))
        
    return -1

# Minimum Time to Visit a Cell In a Grid
def minimumTime(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1
    seen = set()
    
    heap = [(0, 0, 0)]
    while heap:
        steps, row, col = heapq.heappop(heap)
        if row == rows - 1 and col == cols - 1:
            return steps
        if (row, col) in seen:
            continue
        seen.add((row, col))
        for d_row, d_col in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_row, next_col = row+d_row, col+d_col
            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in seen:
                wait_steps = 0
                if (grid[next_row][next_col] - steps) % 2 == 0:
                    wait_steps = 1
                next_steps = max(grid[next_row][next_col] + wait_steps, steps + 1)
                heapq.heappush(heap, (next_steps, next_row, next_col))
        
    return -1