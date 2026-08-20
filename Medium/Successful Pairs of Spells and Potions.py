# Successful Pairs of Spells and Potions
# O(nlogn), O(1)
def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    n = len(potions)
    res = []
    for s in spells:
        l, r = 0, n
        while l < r:
            mid = l+((r-l)>>1)
            if potions[mid] * s >= success:
                r = mid
            else:
                l = mid + 1
        res.append(n-l)
    return res