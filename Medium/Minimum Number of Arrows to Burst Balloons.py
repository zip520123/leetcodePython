# Minimum Number of Arrows to Burst Balloons
# O(n log n), O(n)
def findMinArrowShots(self, points: List[List[int]]) -> int:
    arr = sorted(points)
    res = len(arr)
    curr = arr[0][1]
    for i in range(1, len(arr)):
        if curr >= arr[i][0]:
            res -= 1
            curr = min(curr,arr[i][1])
        else:
            curr = arr[i][1]
    return res

# O(n log n), O(n)
def findMinArrowShots(self, points: List[List[int]]) -> int:
    arr = sorted(points)
    res = 0
    curr = -math.inf
    for i in range(len(arr)):
        if arr[i][0] > curr:
            res += 1
            curr = max(curr, arr[i][1])
        else:
            curr = min(curr, arr[i][1])
    return res