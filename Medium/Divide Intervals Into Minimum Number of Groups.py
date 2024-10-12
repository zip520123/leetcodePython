# Divide Intervals Into Minimum Number of Groups
# O(n log n), O(n)
def minGroups(self, intervals: List[List[int]]) -> int:
    arr = []
    for interval in intervals:
        arr.append((interval[0], 1))
        arr.append((interval[1]+1, -1))

    arr.sort()
    
    res = 0
    curr_max_connection = 0
    for item in arr:
        curr_max_connection += item[1]
        res = max(res, curr_max_connection)
    return res