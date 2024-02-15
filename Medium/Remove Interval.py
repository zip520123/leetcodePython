# Remove Interval
# O(n), O(1)
def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    res = []
    start, end = toBeRemoved[0], toBeRemoved[1]
    for interval in intervals:
        if interval[1] < start or end < interval[0]:
            res.append(interval)
        else:
            if interval[0] < start:
                res.append([interval[0], start])
            if end < interval[1]:
                res.append([end, interval[1]])
    return res