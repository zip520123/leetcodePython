# Sum of All Subset XOR Totals
# O(2^n), O(2^n)
def subsetXORSum(self, nums: List[int]) -> int:
    res = 0

    def dfs(path, index):
        nonlocal res
        if index == len(nums):
            res += path
            return
        dfs(path, index+1)
        dfs(path ^ nums[index], index+1)

    dfs(0,0)

    return res

# O(2^n), O(2^n), FP
def subsetXORSum(self, nums: List[int]) -> int:
    
    def dfs(path, index) -> int:
        if index == len(nums): return path
        curr = 0
        curr += dfs(path ^ nums[index], index + 1)
        curr += dfs(path, index + 1) 
        return curr

    return dfs(0,0)

def subsetXORSum(self, nums: List[int]) -> int:
    def dfs(path, index) -> int:
        if index == len(nums): return path
        return dfs(path ^ nums[index], index + 1) + dfs(path, index + 1) 
    return dfs(0,0)

# O(n)
def subsetXORSum(self, nums: List[int]) -> int:
    result = 0

    for num in nums:
        result |= num

    return result << (len(nums) - 1)