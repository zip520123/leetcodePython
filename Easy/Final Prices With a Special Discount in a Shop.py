# Final Prices With a Special Discount in a Shop
# O(n)
def finalPrices(self, prices: List[int]) -> List[int]:
    stack = []
    res = [ n for n in prices ]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            idx = stack.pop(-1)
            res[idx] = prices[idx] - prices[i]
        stack.append(i)
    return res