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

# O(n), O(1)
def minCostClimbingStairs(self, cost: List[int]) -> int:
    m1 = cost[0]
    m2 = cost[1]
    for i in range(2, len(cost)):
        tempM2 = m2
        m2 = min(m1, m2) + cost[i]
        m1 = tempM2
    return min(m1, m2)