# Furthest Building You Can Reach
# O(n log n), O(n)
def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    n = len(heights)
    i = 0
    heap = []
    while i < n-1:
        if heights[i] < heights[i+1]:
            d = heights[i+1]-heights[i]
            heapq.heappush(heap, d)
            if len(heap) > ladders:
                curr = heapq.heappop(heap)
                bricks -= curr
                if bricks < 0:
                    return i
        i += 1
    return i