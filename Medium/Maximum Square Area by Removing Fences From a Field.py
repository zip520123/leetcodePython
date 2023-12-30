# Maximum Square Area by Removing Fences From a Field
# O(m^2 + n^2), O(m^2+n^2)
def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    mod = 10**9+7
    s1, s2 = set(), set()
    hFences.extend([1,m])
    vFences.extend([1,n])
    hFences.sort()
    vFences.sort()

    for i in range(len(hFences)):
        for j in range(i+1, len(hFences)):
            s1.add(hFences[j]-hFences[i])
    
    for i in range(len(vFences)):
        for j in range(i+1, len(vFences)):
            s2.add(vFences[j]-vFences[i])

    res = 0
    for i in s1:
        if i in s2:
            res = max(res, i*i)
    
    if res == 0: return -1
    return res % mod

def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    mod = 10**9+7
    s1, s2 = set(), set()
    hFences.extend([1,m])
    vFences.extend([1,n])
    hFences.sort()
    vFences.sort()

    for i in range(len(hFences)):
        for j in range(0, i):
            s1.add(hFences[i]-hFences[j])

    for i in range(len(vFences)):
        for j in range(0, i):
            s2.add(vFences[i]-vFences[j])

    res = 0
    for i in s1:
        if i in s2:
            res = max(res, i*i)
    
    if res == 0: return -1
    return res % mod