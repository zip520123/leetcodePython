# Longest Subarray With Maximum Bitwise AND
# O(n), O(1)
def longestSubarray(self, nums: List[int]) -> int:
    res = 1
    curr = 1
    maxN = max(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] and nums[i] == maxN:
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res
