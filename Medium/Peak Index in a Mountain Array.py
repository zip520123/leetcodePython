# Peak Index in a Mountain Array
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    l,r = 0, len(arr)-1
    while l<r:
        mid = l+((r-l)>>1)
        if arr[mid] < arr[mid+1]:
            l = mid+1
        else:
            r = mid
    return l