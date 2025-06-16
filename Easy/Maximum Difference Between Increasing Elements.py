# Maximum Difference Between Increasing Elements
# O(n), O(1)
def maximumDifference(self, nums: List[int]) -> int:
    res = -1
    minP = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[minP]:
            res = max(res, nums[i] - nums[minP])
        if nums[i] < nums[minP]:
            minP = i
    return res