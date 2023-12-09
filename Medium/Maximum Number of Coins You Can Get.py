# Maximum Number of Coins You Can Get
# O(n log n), O(1)
def maxCoins(self, piles: List[int]) -> int:
    res = 0
    piles.sort()
    while piles:
        piles.pop(-1)
        res += piles.pop(-1)
        piles.pop(0)
    return res


# O(n log n), O(1)
def maxCoins(self, piles: List[int]) -> int:
    res = 0
    piles.sort()
    n = len(piles)
    for i in range(n//3,n,2):
        res += piles[i]
    return res