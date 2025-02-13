# Minimum Operations to Exceed Threshold Value II
# O(n log n), O(n)
def minOperations(self, nums: List[int], k: int) -> int:
    heap = [n for n in nums]
    heapq.heapify(heap)
    op = 0
    while heap[0] < k and len(heap) >= 2:
        op += 1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a * 2 + b)
    
    return op