# Maximum Candies Allocated to K Children
# O(n log n), O(1)
def maximumCandies(self, candies: List[int], k: int) -> int:
    
    def isOkay(mid) -> bool:
        if mid == 0:
            return True
        count = 0
        for candy in candies:
            count += candy // mid
        return count >= k
    res = 0
    l, r = 0, max(candies)
    while l<=r:
        mid = l+((r-l)>>1)
        if isOkay(mid):
            res = max(res, mid)
            l = mid + 1
        else:
            r = mid - 1
    return res