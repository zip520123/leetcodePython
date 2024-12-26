# Target Sum
# O(2^n) time complexity, O(n) space complexity
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def dfs(index, count) -> int:
        if index == len(nums):
            if count == target:
                return 1
            return 0
        return dfs(index+1, count + nums[index]) + dfs(index+1, count - nums[index])
    
    return dfs(0, 0)