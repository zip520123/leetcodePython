# Count Number of Maximum Bitwise-OR Subsets
# O(2^n), O(2^n)
def countMaxOrSubsets(self, nums: List[int]) -> int:
    memo = defaultdict(int)
    n = len(nums)
    def dfs(index, path):
        if index == n:
            memo[path] += 1
            return
        dfs(index+1, path)            
        dfs(index+1, path | nums[index])

    dfs(0, 0)
    return max(memo.values())