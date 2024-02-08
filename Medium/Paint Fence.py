# Paint Fence
# O(n^2), O(n) TLE
def numWays(self, n: int, k: int) -> int:
    if n == 0: return 0
    if n == 1: return k
    if n == 2: return k*k

    return (self.numWays(n-2, k) + self.numWays(n-1, k)) * (k-1)

    '''
    numWays(i) = same(i) + diff(i)
    diff(i) = numWays(i-1) * (k-1)
    same(i) = diff(i-1) * 1

    numWays(i) = numWays(i-2) * (k-1) + numWays(i-1) * (k-1)
    numWays(i) = (numWays(i-2) + numWays(i-1)) * (k-1)
    '''
# O(n), O(n)
def numWays(self, n: int, k: int) -> int:
    if n == 0: return 0
    if n == 1: return k
    if n == 2: return k*k

    dp = [0]*(n+1)
    dp[1] = k
    dp[2] = k*k
    for i in range(3,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) * (k-1)
    return dp[n]