# Last Moment Before All Ants Fall Out of a Plank
# O(n), O(1)
def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    res = 0
    for num in left:
        res = max(res, num)
    for num in right:
        res = max(res, n-num)
    return res
