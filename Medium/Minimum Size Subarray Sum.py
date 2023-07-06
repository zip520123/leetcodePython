# Minimum Size Subarray Sum
# O(n), O(1)
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    res = float('inf')
    l, r = 0,0
    n = len(nums)
    sum = 0
    while r<n:
        sum += nums[r]
        while sum >= target:
            res = min(res, r-l+1)
            sum -= nums[l]
            l += 1
        r += 1
    
    return 0 if res == float('inf') else res
        