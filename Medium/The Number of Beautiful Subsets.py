# The Number of Beautiful Subsets
# O(2^n),O(n)
def beautifulSubsets(self, nums: List[int], k: int) -> int:
    res = 0
    
    def dfs(path, index: int):
        nonlocal res
        if path:
            res += 1
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            if len(path) == 0 or all(abs(n-nums[i]) != k for n in path):
                new_path = path.copy()
                new_path.add(nums[i])
                dfs(new_path, i + 1)
            
    dfs(set(),0)
    return res