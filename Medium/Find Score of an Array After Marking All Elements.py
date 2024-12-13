# Find Score of an Array After Marking All Elements
# O(n log n), O(n)
def findScore(self, nums: List[int]) -> int:
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, (nums[i], i))
    
    res = 0
    seen = set()
    while heap:
        curr_n, curr_index = heapq.heappop(heap)
        if curr_index not in seen:
            res += curr_n
            seen.add(curr_index + 1)
            seen.add(curr_index - 1)
    
    return res