# Element Appearing More Than 25% In Sorted Array
# O(n), O(1)
def findSpecialInteger(self, arr: List[int]) -> int:
    n = len(arr)
    curr = 1
    for i in range(n):
        if i == 0 or arr[i-1] != arr[i]:
            curr = 1
        else:
            curr += 1
        if curr > n/4:
            return arr[i]
    return 0