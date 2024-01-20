# Divide an Array Into Subarrays With Minimum Cost I
# O(n), O(n)
def minimumCost(self, nums: List[int]) -> int:
    res = math.inf
    n = len(nums)
    for i in range(1, n-1):
        for j in range(i+1, n):
            res = min(res, nums[0]+nums[i]+nums[j])
    return res