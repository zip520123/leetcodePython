# Maximum Distance in Arrays
# O(n), O(1)
def maxDistance(self, arrays: List[List[int]]) -> int:
    res = 0
    curr_min, curr_max = arrays[0][0], arrays[0][-1]
    for i in range(1, len(arrays)):
        res = max(res, abs(curr_min - arrays[i][-1]), abs(curr_max - arrays[i][0]))
        curr_min = min(curr_min, arrays[i][0])
        curr_max = max(curr_max, arrays[i][-1])
    return res

# O(n^2), O(1) TLE
def maxDistance(self, arrays: List[List[int]]) -> int:
    res = 0
    for i in range(len(arrays)):
        for j in range(len(arrays)):
            if i != j:
                res = max(res, abs(arrays[i][0]-arrays[j][0]))
                res = max(res, abs(arrays[i][-1]-arrays[j][0]))
                res = max(res, abs(arrays[i][0]-arrays[j][-1]))
                res = max(res, abs(arrays[i][-1]-arrays[j][-1]))
    return res

