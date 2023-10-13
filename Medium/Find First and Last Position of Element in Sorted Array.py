# Find First and Last Position of Element in Sorted Array
# O(log n), O(1)
def searchRange(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    if n == 0: return [-1,-1]
    l, r = 0, n-1
    while l<r:
        mid = l+((r-l)>>1)
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid
    if nums[l] != target: return [-1,-1]
    res = [l]
    l = 0; r = n
    while l<r:
        mid = l+((r-l)>>1)
        if nums[mid] <= target:
            l = mid+1
        else:
            r = mid
    res.append(l-1)
    return res