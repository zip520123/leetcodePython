# Subsets
# O(2^n), O(2^n)
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(path, index):
        if index == len(nums):
            res.append(path)
            return
        dfs(path, index + 1)
        dfs(path + [nums[index]], index + 1)
    dfs([],0)
    return res

# O(2^n), O(2^n)
def subsets(self, nums: List[int]) -> List[List[int]]:
    
    def dfs(path, index) -> List[List[int]]:
        if index == len(nums):
            return [path]
        res = []
        res += dfs(path, index + 1)
        res += dfs(path + [nums[index]], index + 1)
        return res
    
    return dfs([],0)

def subsets(self, nums: List[int]) -> List[List[int]]:
    
    def dfs(path, index) -> List[List[int]]:
        if index == len(nums):
            return [path]
        return dfs(path, index + 1) + dfs(path + [nums[index]], index + 1)
    
    return dfs([],0)