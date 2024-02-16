# Missing Ranges
# O(n), O(n)
def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
    res = []
    n = len(nums)
    if n == 0: return [[lower, upper]]
    for i in range(n-1):
        l, r = nums[i]+1, nums[i+1]-1
        if l<=r:
            res.append([l,r])
    if lower < nums[0]:
        res =  [[lower, nums[0]-1]] + res
    if nums[n-1] < upper:
        res.append([nums[n-1]+1, upper])
    return res