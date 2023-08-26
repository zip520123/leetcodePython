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

# O(n log n), O(1), greedy
def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs.sort(key= lambda x: x[1])
    curr = float('-inf')
    res = 0
    for pair in pairs:
        if curr < pair[0]:
            res += 1
            curr = pair[1]
    return res