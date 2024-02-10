# Merge Intervals
# O(n log n), O(n)
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    intervals.sort()
    for i in range(len(intervals)):
        start, end = intervals[i]
        if len(res) != 0 and res[-1][1] >= start:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append(intervals[i])
    return res