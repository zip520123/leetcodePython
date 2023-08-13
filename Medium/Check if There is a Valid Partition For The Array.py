# Check if There is a Valid Partition For The Array
# O(n), O(n)
def validPartition(self, nums: List[int]) -> bool:
    map = {}
    n = len(nums)
    def dfs(i: int) -> bool:
        if i in map: return map[i]
        if i == n: return True
        res = False
        if i+1 < n and nums[i] == nums[i+1]:
            res = res or dfs(i+2)
        if i+2 < n and nums[i] == nums[i+1] == nums[i+2]:
            res = res or dfs(i+3)
        if i+2 < n and nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1:
            res = res or dfs(i+3)
        map[i] = res
        return res
    return dfs(0)

def validPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    @cache
    def dfs(i: int) -> bool:
        if i == n: return True
        res = False
        if i+1 < n and nums[i] == nums[i+1]:
            res = res or dfs(i+2)
        if i+2 < n and nums[i] == nums[i+1] == nums[i+2]:
            res = res or dfs(i+3)
        if i+2 < n and nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1:
            res = res or dfs(i+3)
        return res
    return dfs(0)