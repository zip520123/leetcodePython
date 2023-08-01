# Combinations
# O(n^k), O(n^k)
def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    def dfs(curr: List[int], currN: int):
        if len(curr) == k:
            res.append(curr)
            return
        for i in range(currN, n+1):
            dfs(curr+[i], i+1)
    
    dfs([],1)
    return res