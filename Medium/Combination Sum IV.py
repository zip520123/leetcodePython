# Combination Sum IV
# O(n), O(n)
def combinationSum4(self, nums: List[int], target: int) -> int:
    @cache
    def dfs(curr: int) -> int:
        if curr == 0 : return 1
        res = 0
        for n in nums:
            if curr-n >= 0:
                res += dfs(curr-n)

        return res
    return dfs(target)