# Largest Positive Integer That Exists With Its Negative
# O(n log n), O(n)
def findMaxK(self, nums: List[int]) -> int:
    nums_set = set()
    heap = []
    for n in nums:
        if n > 0:
            nums_set.add(n)
        else:
            heapq.heappush(heap, n)
    while heap:
        curr = heapq.heappop(heap)
        if -curr in nums_set:
            return -curr
    return -1