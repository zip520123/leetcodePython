# Search Insert Position
# O(log n), O(1)
def searchInsert(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l<r:
        mid = l+((r-l)>>1)
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l