# Insert Interval
# O(n), O(n)
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    if n == 0: return [newInterval]
    if newInterval[-1] < intervals[0][0]:
        return [newInterval] + intervals
    res = []
    for i in range(n):
        interval = intervals[i]
        res.append(interval)
        last = res[-1]
        if self.is_overlap(last, newInterval):
            res.pop(-1)
            res.append([min(last[0], newInterval[0]), max(last[1], newInterval[1])])
            for j in range(i+1, n):
                if self.is_overlap(res[-1], intervals[j]):
                    res[-1] = [min(res[-1][0], intervals[j][0]), max(res[-1][1], intervals[j][1])]
                else:
                    res.append(intervals[j])
            return res
        elif last[1] < newInterval[0] and i+1 < n and newInterval[1] < intervals[i+1][0]:
            res.append(newInterval)
            for j in range(i+1, n):
                res.append(intervals[j])
            return res
    res.append(newInterval)
    return res

def is_overlap(self, interval1: List[int], interval2: List[int]) -> bool:
    if interval1[0] < interval2[0]:
        if interval1[1] < interval2[0]:
            return False
        
    elif interval2[0] < interval1[0]:
        if interval2[1] < interval1[0]:
            return False
    return True