# Maximum Length of Pair Chain
# O(n^2), O(n)
def findLongestChain(self, pairs: List[List[int]]) -> int:
    n = len(pairs)
    pairs.sort()

    memo = {}
    def dfs(i: int) -> int:
        if i in memo: 
            return memo[i]
        res = 1
        for j in range(i+1,n):
            if pairs[i][1] < pairs[j][0]:
                res = max(res, dfs(j) + 1)
        memo[i] = res
        return res
    
    res = 0
    for i in range(n):
        res = max(res, dfs(i))
    return res