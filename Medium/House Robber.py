# House Robber
# O(n), O(n)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]
    if n == 2: return max(nums[0],nums[1])
    nums[1] = max(nums[0],nums[1])
    for i in range(2,n):
        nums[i] = max(nums[i]+nums[i-2], nums[i-1])
    return nums[n-1]

# O(n), O(1)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]
    if n == 2: return max(nums[0],nums[1])
    dp1, dp2 = nums[0], max(nums[0],nums[1])

    for num in nums[2:]:
        t = max(dp1+num, dp2)
        dp1 = dp2
        dp2 = t
    return dp2