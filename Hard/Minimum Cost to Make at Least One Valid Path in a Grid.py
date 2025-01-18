# Minimum Cost to Make at Least One Valid Path in a Grid
# O(n*m) time O(n*m) space
def minCost(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [ [math.inf]*cols for _ in range(rows) ]
    dp[0][0] = 0
    heap = [(0,0,0)]
    while heap:
        cost, row, col = heapq.heappop(heap)
        direction = grid[row][col]
        if row == rows-1 and col == cols - 1:
            return cost
        if col + 1 < cols:
            next_cell_cost = cost
            if direction != 1:
                next_cell_cost += 1

            if next_cell_cost < dp[row][col+1]:
                dp[row][col+1] = next_cell_cost
                heapq.heappush(heap, (next_cell_cost, row, col + 1))
        if row + 1 < rows:
            next_cell_cost = cost
            if direction != 3:
                next_cell_cost += 1
            if next_cell_cost < dp[row+1][col]:
                dp[row+1][col] = next_cell_cost
                heapq.heappush(heap, (next_cell_cost, row + 1, col))
        if col - 1 >= 0:
            next_cell_cost = cost
            if direction != 2:
                next_cell_cost += 1
            if next_cell_cost < dp[row][col-1]:
                dp[row][col-1] = next_cell_cost
                heapq.heappush(heap, (next_cell_cost, row , col-1))

        if row - 1 >= 0:
            next_cell_cost = cost
            if direction != 4:
                next_cell_cost += 1
            if next_cell_cost < dp[row-1][col]:
                dp[row-1][col] = next_cell_cost
                heapq.heappush(heap, (next_cell_cost, row-1 , col))
    return -1