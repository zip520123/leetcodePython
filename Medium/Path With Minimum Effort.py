# Path With Minimum Effort
# O(n log n), O(n)
def minimumEffortPath(self, heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    memo = defaultdict(lambda: math.inf)
    memo[(0,0)] = 0
    minHeap = [(0,0,0)]

    while minHeap:
        effort, x, y = heappop(minHeap)
        if x == rows-1 and y == cols-1: return effort

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < rows and 0 <= ny < cols:
                neffort = max(effort, abs(heights[x][y]-heights[nx][ny]))
                if neffort < memo[(nx,ny)]:
                    memo[(nx,ny)] = neffort
                    heappush(minHeap, (neffort, nx,ny))