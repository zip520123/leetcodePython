# Non-overlapping Intervals
# O(n log n), O(1)
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    arr = sorted(intervals, key=lambda x: x[0])
    l, r = 0, 1
    res = 0
    while r < len(arr):
        if arr[l][1] <= arr[r][0]:
            l = r
        else:
            res += 1
            if arr[l][1] > arr[r][1]:
                l = r
        r += 1
    return res