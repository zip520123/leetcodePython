# Subarray Product Less Than K
# O(n), O(1)
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    res, p = 0, 1
    l, r = 0, 0
    while r<len(nums):
        p *= nums[r]
        while p >= k and l <= r:
            p /= nums[l]
            l += 1
        res += r-l+1
        r += 1
    return res