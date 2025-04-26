# Interval List Intersections
# O(list1*list2), O(1)
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    res = []

    for list1 in firstList:
        for list2 in secondList:
            a = max(list1[0], list2[0])
            b = min(list1[1], list2[1])
            if a<=b:
                res.append([a,b])
    return res

# O(list1+list2), O(1)
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    res = []
    l, r = 0, 0
    while l<len(firstList) and r < len(secondList):
        a = max(firstList[l][0], secondList[r][0])
        b = min(firstList[l][1], secondList[r][1])
        if a <= b:
            res.append([a,b])
        if firstList[l][1] < secondList[r][1]:
            l += 1
        else:
            r += 1
    
    return res