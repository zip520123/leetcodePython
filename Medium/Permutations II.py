# Permutations II
# O(n!), O(n!)
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(arr, path):
        if len(arr) == 0:
            res.append(path)
            return
        prev = None
        for i in range(len(arr)):
            if arr[i] == prev: continue
            prev = arr[i]
            dfs(arr[:i]+arr[i+1:], path+[arr[i]])
    dfs(sorted(nums), [])
    return res

# O(n!), O(n)
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    counter = Counter(nums)
    def dfs(path):
        if len(path) == len(nums):
            res.append(path)
            return
        for num in counter:
            if counter[num] > 0:
                counter[num] -= 1
                dfs(path+[num])
                counter[num] += 1
    dfs([])
    return res