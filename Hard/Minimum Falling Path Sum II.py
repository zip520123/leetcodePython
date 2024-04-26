# Minimum Falling Path Sum II
# O(rows*cols*cols), O(1)
def minFallingPathSum(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    for row in range(1, rows):
        
        for col_index in range(cols):
            prev_min = math.inf
            for prev_col_index in range(cols):
                if col_index != prev_col_index:
                    prev_min = min(prev_min, grid[row-1][prev_col_index])
            grid[row][col_index] += prev_min

    return min(grid[rows-1])

# O(rows * cols * (log cols)), O(cols)
def minFallingPathSum(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    heap = []
    for col in range(cols):
        heapq.heappush(heap, (grid[0][col], col))
    
    for row in range(1, rows):
        nextHeap = []
        for col in range(cols):
            prev_min, prev_index = heapq.heappop(heap)
            if col == prev_index:
                second_min, second_prev_index = heapq.heappop(heap)
                heapq.heappush(nextHeap, (grid[row][col] + second_min, col))
                heapq.heappush(heap, (second_min, second_prev_index))
            else:
                heapq.heappush(nextHeap, (grid[row][col] + prev_min, col))
            heapq.heappush(heap, (prev_min, prev_index))
        heap = nextHeap

    return heap[0][0]