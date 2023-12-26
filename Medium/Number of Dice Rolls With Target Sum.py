# Number of Dice Rolls With Target Sum
# O(n*k), O(n*k)
def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    mod = 1E9+7

    @cache
    def dfs(curr, i):
        if i == n:
            if curr == target: return 1
            return 0
        res = 0
        for point in range(1,k+1):
            res += dfs(point+curr, i+1) 
        return int(res % mod)
    return dfs(0,0)


def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    mod = 1E9+7
    memo = {}
    
    def dfs(curr, i):
        if (curr,i) in memo: return memo[(curr,i)]
        if i == n:
            if curr == target: return 1
            return 0
        res = 0
        for point in range(1,k+1):
            res += dfs(point+curr, i+1) 
        memo[(curr,i)] = int(res % mod)
        return int(res % mod)
    return dfs(0,0)


# O(n*k*target), O(n*target)
def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    mod = 1E9+7
    dp = [[0]*(target+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for point in range(1,k+1):
            for currTarget in range(1, target+1):
                if point <= currTarget:
                    dp[i][currTarget] = (dp[i][currTarget] + dp[i-1][currTarget-point]) % mod
    return int(dp[n][target])