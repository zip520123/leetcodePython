# Maximum Coins From K Consecutive Bags
# O(n log n), O(n)
def maximumCoins(self, coins: List[List[int]], k: int) -> int:
    coins.sort()
    res = 0
    i, j, n = 0, 0, len(coins)
    curr_sum = 0
    while i<n:
        while j < n and coins[j][1] < coins[i][0] + k:
            curr_sum += (coins[j][1] - coins[j][0] + 1) * coins[j][2]
            j += 1
        if j < n:
            partial = (coins[i][0] + k - 1 - coins[j][0] + 1) * coins[j][2]
            res = max(res, curr_sum + partial)
        curr_sum -= (coins[i][1] - coins[i][0] + 1) * coins[i][2]
        i += 1

    i, j, curr_sum = 0, 0, 0
    while i<n:
        curr_sum += (coins[i][1] - coins[i][0] + 1) * coins[i][2]

        while j < n and coins[j][1] < coins[i][1] - k + 1:
            curr_sum -= (coins[j][1] - coins[j][0] + 1) * coins[j][2]
            j += 1

        partial = max(0, (coins[i][1] - k + 1 - coins[j][0]) * coins[j][2])
        res = max(res, curr_sum - partial)
        i += 1
    return res