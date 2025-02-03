# Longest Strictly Increasing or Strictly Decreasing Subarray
# O(n), O(1)
def longestMonotonicSubarray(self, nums: List[int]) -> int:
    res = 1
    curr = 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            curr += 1
        else:
            curr = 1
        res = max(res, curr)
    curr = 1
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            curr += 1
        else:
            curr = 1
        res = max(res, curr)
    return res