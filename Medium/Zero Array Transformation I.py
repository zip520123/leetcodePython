# Zero Array Transformation I
# O(nums + queries), O(nums)
def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    dp = [0] * (n + 1)
    for l, r in queries:
        dp[l] += 1
        dp[r+1] -= 1
    curr = 0
    for i in range(n):
        curr += dp[i]
        if nums[i] > curr:
            return False
    return True