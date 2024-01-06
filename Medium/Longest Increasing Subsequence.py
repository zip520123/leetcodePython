# Longest Increasing Subsequence
# O(n^2), O(n)
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    res = 1
    for i in range(1,n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])

    return res

# O(n log n), O(n)
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = []
    for n in nums:
        l, r = 0, len(dp)
        while l<r:
            mid = l+((r-l)>>1)
            if dp[mid] < n:
                l = mid+1
            else:
                r = mid
        if l == len(dp):
            dp.append(n)
        else:
            dp[l] = n
    return len(dp)