# Minimum Cost to Connect Sticks
# O(n log n), O(n)
def connectSticks(self, sticks: List[int]) -> int:
    res = 0
    heap = sticks.copy()
    heapq.heapify(heap)
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        curr = a+b
        res += curr
        heapq.heappush(heap, curr)
    return res