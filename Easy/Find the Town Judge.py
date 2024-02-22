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

# O(n), O(n)
def findJudge(self, n: int, trust: List[List[int]]) -> int:
    memo1 = defaultdict(int)
    memo2 = defaultdict(int)
    for a,b in trust:
        memo1[a] += 1
        memo2[b] += 1
    res = None
    for p in range(1,n+1):
        if memo1[p] == 0 and memo2[p] == n-1:
            if res != None:
                return -1
            res = p
    if res == None:
        return -1
    return res