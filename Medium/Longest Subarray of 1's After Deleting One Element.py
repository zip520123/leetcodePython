# Longest Subarray of 1's After Deleting One Element
# O(n), O(1)
def longestSubarray(self, nums: List[int]) -> int:
    l, r = 0,0
    n = len(nums)
    count = 0
    res = 0
    while r<n:
        if nums[r] == 0:
            count += 1
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
        res = max(res, r-l+1)
        r += 1
    return res-1