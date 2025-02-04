# Maximum Ascending Subarray Sum
# O(n), O(1)
def maxAscendingSum(self, nums: List[int]) -> int:
    curr, res = nums[0], nums[0]
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            curr += nums[i+1]
        else:
            curr = nums[i+1]
        res = max(res, curr)
    return res