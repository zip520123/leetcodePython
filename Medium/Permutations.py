# Permutations
# O(n!), O(n!)
def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(arr: List[int], path: List[int]):
        if len(arr) == 0:
            res.append(path)
            return
        for i in range(len(arr)):
            dfs(arr[:i]+arr[i+1:], path+[arr[i]])
    dfs(nums, [])

    return res