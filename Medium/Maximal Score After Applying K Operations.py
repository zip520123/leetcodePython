# Maximal Score After Applying K Operations
# O(n log n), O(n)
def maxKelements(self, nums: List[int], k: int) -> int:
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)
    res = 0
    for _ in range(k):
        curr = -heapq.heappop(heap)
        res += curr 
        heapq.heappush(heap, -math.ceil(curr/3))
    return res