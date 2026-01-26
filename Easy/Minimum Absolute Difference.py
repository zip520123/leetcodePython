# Minimum Absolute Difference
# O(n log n), O(n)
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    res = []
    currabs = abs(arr[1]-arr[0])
    for i in range(len(arr)-1):
        if currabs == abs(arr[i+1]-arr[i]):
            res.append([arr[i], arr[i+1]])
        elif currabs > abs(arr[i+1]-arr[i]):
            currabs = arr[i+1]-arr[i]
            res = [[arr[i], arr[i+1]]]
    return res