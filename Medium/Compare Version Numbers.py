# Compare Version Numbers
# O(n), O(n)
def compareVersion(self, version1: str, version2: str) -> int:
    arr1, arr2 = list(map(int, version1.split("."))), list(map(int, version2.split(".")))
    l, r = 0, 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            return -1
        if arr1[l] > arr2[r]:
            return 1
        l += 1
        r += 1
    while l < len(arr1):
        if arr1[l] > 0:
            return 1
        l += 1
    while r < len(arr2):
        if arr2[r] > 0:
            return -1
        r += 1
    return 0