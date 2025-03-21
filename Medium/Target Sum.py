# Target Sum
# O(2^n) time complexity, O(n) space complexity, TLE
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def dfs(index, count) -> int:
        if index == len(nums):
            if count == target:
                return 1
            return 0
        return dfs(index+1, count + nums[index]) + dfs(index+1, count - nums[index])
    
    return dfs(0, 0)

# O(n*sum) time complexity, O(n*sum) space complexity
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    @cache
    def dfs(index, count) -> int:
        if index == len(nums):
            if count == target:
                return 1
            return 0
        return dfs(index+1, count + nums[index]) + dfs(index+1, count - nums[index])
    
    return dfs(0, 0)

# O(n*sum) time complexity, O(n*sum) space complexity
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    memo = {}
    def dfs(index, count) -> int:
        if (index, count) in memo:
            return memo[(index, count)]
        if index == len(nums):
            if count == target:
                return 1
            return 0
        memo[(index, count)] = dfs(index+1, count + nums[index]) + dfs(index+1, count - nums[index])
        return memo[(index,count)]
    
    return dfs(0, 0)