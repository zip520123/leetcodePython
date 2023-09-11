# Group the People Given the Group Size They Belong To
# O(n), O(n)
def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    map = {}
    res = []
    for i,n in enumerate(groupSizes):
        if n not in map:
            map[n] = []
        map[n].append(i)
        if len(map[n]) == n:
            res.append(map[n])
            map[n] = []
    return res