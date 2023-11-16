# Maximum Element After Decreasing and Rearranging
# O(n log n), O(n)
def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    arr.sort()
    arr2 = arr
    if arr2[0] != 1: arr2[0] = 1
    for i in range(1,len(arr2)):
        if abs(arr2[i]-arr2[i-1]) > 1: 
            arr2[i] = arr2[i-1] + 1
    return arr2[-1]