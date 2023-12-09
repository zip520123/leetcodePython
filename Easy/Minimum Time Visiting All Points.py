# Minimum Time Visiting All Points
# O(n), O(1)
def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    res = 0
    n = len(points)
    for i in range(1,n):
        p1 = points[i-1]
        p2 = points[i]
        res += max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))
    return res