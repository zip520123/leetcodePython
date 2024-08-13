# Combination Sum II
# O(2^n), O(n), TLE
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)

    def dfs(curr_sum: int, path: [int], index: int) -> List[List[int]]:
        if curr_sum == target:
            return [path]
        if index == n:
            if curr_sum == target:
                return [path]
            else:
                return []
        res = []
        prev = None
        for i in range(index, n):
            if prev == candidates[i]: continue
            prev = candidates[i]
            res += dfs(curr_sum + candidates[i], path + [candidates[i]], i+1)
        return res
    
    return dfs(0, [], 0)

# O(2^n), O(n)
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)

    def dfs(curr_sum: int, path: [int], index: int) -> List[List[int]]:
        if curr_sum >= target:
            if curr_sum == target:
                return [path]
            else:
                return []

        res = []
        prev = None
        for i in range(index, n):
            if prev == candidates[i]: continue
            prev = candidates[i]
            res += dfs(curr_sum + candidates[i], path + [candidates[i]], i+1)
        return res
    
    return dfs(0, [], 0)