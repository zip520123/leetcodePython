# Count All Valid Pickup and Delivery Options
# O(n), O(1)
def countOrders(self, n: int) -> int:
    res = 1
    for i in range(1,n+1):
        res *= i
        res *= 2 * i - 1
        res %= 1E9+7
    return int(res)