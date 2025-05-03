# Minimum Domino Rotations For Equal Row
# O(n), O(1)
def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    n = len(tops)
    res = math.inf
    for curr in range(1,6+1):
        count = 0
        change = 0
        for i in range(n):
            if tops[i] == curr:
                count += 1
            elif bottoms[i] == curr:
                change += 1
        if count + change == n:
            res = min(res, change)
    for curr in range(1,6+1):
        count = 0
        change = 0
        for i in range(n):
            if bottoms[i] == curr:
                count += 1
            elif tops[i] == curr:
                change += 1
        if count + change == n:
            res = min(res,  change)
    if res == math.inf:
        return -1
    return res