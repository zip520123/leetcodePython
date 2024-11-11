# Jump Game II
# O(n*m), O(n)
def jump(self, nums: List[int]) -> int:
    dp = [math.inf] * len(nums)
    dp[0] = 0
    for i in range(len(nums)):
        curr = nums[i]
        for next_i in range(i+1, curr+i+1):
            if next_i < len(nums):
                dp[next_i] = min(dp[next_i], dp[i] + 1)
    return dp[-1]

# O(n), O(1)
def jump(self, nums: List[int]) -> int:
    curr_end, next_i = 0, 0
    res = 0
    for i in range(len(nums)-1):
        n = nums[i]
        next_i = max(next_i, i+n)
        if i == curr_end:
            res += 1
            curr_end = next_i
    return res