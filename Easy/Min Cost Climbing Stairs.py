# Min Cost Climbing Stairs
# O(n), O(1)
def minCostClimbingStairs(self, cost: List[int]) -> int:
    arr = cost + [0]
    dp1, dp2 = 0, 0
    n = len(arr)
    for i in range(2, n):
        t = min(dp1+arr[i-1], dp2+arr[i-2])
        dp2 = dp1
        dp1 = t
    return dp1