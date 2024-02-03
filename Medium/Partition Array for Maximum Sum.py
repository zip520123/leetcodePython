# Partition Array for Maximum Sum
# O(n^2), O(n)
def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] + [0 for i in range(n)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if i-j >= 0:
                dp[i] = max(dp[i], dp[i-j] + max(arr[i-j:i]) * j)
            
    return dp[-1]

# O(n), O(n)
def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] + [0 for i in range(n)]
    for i in range(1,n+1):
        currN = arr[i-1]
        for j in range(1,k+1):
            if i-j >= 0:
                currN = max(currN, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + currN * j)
            
    return dp[-1]