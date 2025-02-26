# Maximum Absolute Sum of Any Subarray
# O(n), O(n)
def maxAbsoluteSum(self, nums: List[int]) -> int:
    n = len(nums)
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = nums[0]
    dp2[0] = nums[0]
    res = abs(nums[0])
    
    for i in range(1, n):
        dp1[i] = max(dp1[i-1], 0) + nums[i]
        dp2[i] = min(dp2[i-1], 0) + nums[i]
        res = max(res, dp1[i], abs(dp2[i]))
    return res