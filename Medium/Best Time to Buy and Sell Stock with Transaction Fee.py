# Best Time to Buy and Sell Stock with Transaction Fee
# O(n), O(1)
def maxProfit(self, prices: List[int], fee: int) -> int:
    buy = -prices[0]
    keep = -prices[0]
    sell = 0
    n = len(prices)
    for i in range(n):
        prevBuy = buy
        prevKeep = keep
        prevSell = sell
        buy = prevSell-prices[i]
        sell = max(prevSell, max(prevBuy, prevKeep) + prices[i] - fee) 
        keep = max(prevBuy, prevKeep)
    return sell