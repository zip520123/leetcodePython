# Final Prices With a Special Discount in a Shop
# O(n^2), O(1)
def finalPrices(self, prices: List[int]) -> List[int]:
    res = []
    for i in range(len(prices)):
        curr = prices[i]
        discount = 0
        for j in range(i+1, len(prices)):
            if prices[j] <= prices[i]:
                discount = prices[j]
                break
        res.append(curr-discount)
    return res

# O(n), O(n)
def finalPrices(self, prices: List[int]) -> List[int]:
    stack = []
    res = [0] * len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            prev_i = stack.pop(-1)
            res[prev_i] = prices[prev_i] - prices[i]
        stack.append(i)
    for i in stack:
        res[i] = prices[i]
    return res