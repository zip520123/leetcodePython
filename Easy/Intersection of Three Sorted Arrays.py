# Intersection of Three Sorted Arrays
# O(n), O(n)
def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    memo2 = defaultdict(int)
    for n in arr2:
        memo2[n] += 1
    memo3 = defaultdict(int)
    for n in arr3:
        memo3[n] += 1
    res = []
    for n in arr1:
        if n in memo2 and n in memo3:
            res.append(n)
    return res 

# O(n), O(1)
def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    res = []
    p1, p2, p3 = 0,0,0
    while p1<len(arr1) and p2<len(arr2) and p3<len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            if arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3 += 1
    return res 