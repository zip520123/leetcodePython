# Find the Town Judge
# O(n), O(n)
def findJudge(self, n: int, trust: List[List[int]]) -> int:
    arr = [0] * n
    arr2 = [0] * n
    for a, b in trust:
        arr[b-1] += 1
        arr2[a-1] += 1
    res = None
    for i in range(n):
        if arr[i] == n-1 and arr2[i] == 0:
            if res != None: 
                return -1
            res = i+1
    if res == None:
        return -1
    return res