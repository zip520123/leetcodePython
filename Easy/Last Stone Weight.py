# Last Stone Weight
# O(n log n)
def lastStoneWeight(self, stones: List[int]) -> int:
    heap = []
    for s in stones:
        heapq.heappush(heap, -s)

    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a-b > 0:
            heapq.heappush(heap, -(a-b))
    if len(heap) == 0:
        return 0
    return -heap[0]