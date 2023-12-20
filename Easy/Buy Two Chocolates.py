# Buy Two Chocolates
# O(n log n), O(n)
def buyChoco(self, prices: List[int], money: int) -> int:
    arr = sorted(prices)
    p = arr[0] + arr[1]
    if p > money: return money
    return money-p