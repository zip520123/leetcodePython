# Jump Game
# O(n^2), O(n) TLE
def canJump(self, nums: List[int]) -> bool:
    
    dp = [False] * len(nums)
    dp[0] = True
    for i in range(len(nums)):
        if dp[i]:
            curr = nums[i]
            for j in range(1, i+curr+1):
                if j < len(nums):
                    dp[j] = True
    return dp[-1] == True

# O(n), O(1)
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    pos = n-1
    for i in range(n-1, -1, -1):
        if i + nums[i] >= pos:
            pos = i
    return pos == 0