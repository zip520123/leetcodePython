# Minimum Time Difference
# O(n log n), O(n)
def findMinDifference(self, timePoints: List[str]) -> int:
    arr = []
    for time in timePoints:
        mins = (int(time[0]) * 10 + int(time[1])) * 60 + int(time[3]) * 10 + int(time[4])
        arr.append(mins)
    arr.sort()
    day_mins = 24 * 60
    res = math.inf
    for i in range(1, len(arr)):
        res = min(res, arr[i] - arr[i-1])
    res = min(res, arr[0] + day_mins - arr[-1])
    return res