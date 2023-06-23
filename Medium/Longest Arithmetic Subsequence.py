# Longest Arithmetic Subsequence
# O(n^2), O(n^2)
def longestArithSeqLength(self, nums: List[int]) -> int:
    dp = {}
    n = len(nums)
    for i in range(n):
        for j in range(0,i):
            dp[(i, nums[i]-nums[j])] = dp.get((j, nums[i]-nums[j]), 1) + 1
    return max(dp.values())