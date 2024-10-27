# Best Time to Buy and Sell Stock
# O(n), O(1)
def maxProfit(self, prices: List[int]) -> int:
    res = 0
    curr_min = prices[0]
    for p in prices:
        res = max(res, p - curr_min)
        curr_min = min(curr_min, p)
    return res