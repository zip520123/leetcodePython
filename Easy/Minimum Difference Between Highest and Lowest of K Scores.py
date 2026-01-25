# Minimum Difference Between Highest and Lowest of K Scores
# O(n log n), O(1)
def minimumDifference(self, nums: List[int], k: int) -> int:
    nums.sort()
    
    res = math.inf
    for i in range(len(nums)-k+1):
        res = min(res, nums[i+k-1] - nums[i])
    if res == math.inf:
        res = 0
    return res