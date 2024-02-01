# Maximum Subarray
# O(n), O(1)
def maxSubArray(self, nums: List[int]) -> int:
    dp = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        dp = max(dp+nums[i], nums[i])
        res = max(res, dp)
    return res

# O(n), O(1)
def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    curr = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        if curr < 0: curr = 0
        curr += n
        res = max(res, curr)
    return res