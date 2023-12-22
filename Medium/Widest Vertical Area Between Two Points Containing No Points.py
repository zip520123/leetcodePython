# Widest Vertical Area Between Two Points Containing No Points
# O(n log n), O(n)
def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    arr = sorted(points, key=lambda x: x[0])
    res = 0
    for i in range(1, len(arr)):
        res = max(res, arr[i][0]-arr[i-1][0])
    return res