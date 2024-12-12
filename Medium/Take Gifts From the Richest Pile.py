# Take Gifts From the Richest Pile
# O(n log n), O(n)
def pickGifts(self, gifts: List[int], k: int) -> int:
    heap = []
    for n in gifts:
        heapq.heappush(heap, -n)
    
    
    for _ in range(k):
        curr = -heapq.heappop(heap)
        heapq.heappush(heap, -int(sqrt(curr)))
    
    return -sum(heap) 