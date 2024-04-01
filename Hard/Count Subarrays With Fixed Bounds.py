# Count Subarrays With Fixed Bounds
# O(n), O(1)
def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    bad_index = min_index = max_index = -1
    res = 0
    for i in range(len(nums)):
        n = nums[i]
        if not minK <= n <= maxK:
            bad_index = i
        if n == minK:
            min_index = i
        if n == maxK:
            max_index = i
        count = min(min_index, max_index) - bad_index
        if count > 0:
            res += count
    return res