# Sort the People
# O(n log n), O(n)
def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    arr = []
    for i in range(len(names)):
        name, height = names[i], heights[i]
        arr.append((name, height)) 
    arr2 = sorted(arr,key = lambda data: data[1], reverse= True)
    res = []
    for item in arr2:
        res.append(item[0])
    return res