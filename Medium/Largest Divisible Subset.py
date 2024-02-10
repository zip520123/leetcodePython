# Largest Divisible Subset
# O(n^2), O(n^2)
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    dp = [ [n] for n in nums ]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    res = []
    for arr in dp:
        if len(res) < len(arr):
            res = arr
    return res

# Largest Divisible Subset
# O(n^2), O(n)
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    resIndex = 0
    length = 1
    dp = [ [-1, 1] for n in nums ]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i][1] < dp[j][1] + 1:
                dp[i][1] = dp[j][1] + 1
                dp[i][0] = j
            
            if length < dp[i][1]:
                length = dp[i][1]
                resIndex = i

    res = []
    while resIndex != -1:
        res.append(nums[resIndex])
        resIndex = dp[resIndex][0]
    return res