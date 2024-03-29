# Length of Longest Subarray With at Most K Frequency
# O(n), O(n)
def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    res = 0
    l, r = 0, 0
    memo = defaultdict(int)
    while r<len(nums):
        n = nums[r]
        memo[n] += 1
        while memo[n] > k:
            leftN = nums[l]
            memo[leftN] -= 1
            l += 1
        res = max(res, r-l+1)
        r += 1
    return res