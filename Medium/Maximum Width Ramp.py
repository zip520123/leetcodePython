# Maximum Width Ramp
# O(n^2), O(1), TLE
def maxWidthRamp(self, nums: List[int]) -> int:
    res = 0
    n = len(nums)
    for i in range(n-1):
        for j in range(i+res, n):
            if nums[i] <= nums[j]:
                res = max(res, j - i)
    return res

# O(n log n), O(n)
def maxWidthRamp(self, nums: List[int]) -> int:
    
    n = len(nums)
    arr = [ i for i in range(n)]
    arr.sort(key= lambda i: (nums[i], i))

    min_index = math.inf
    width = 0
    for i in arr:
        width = max(width, i-min_index)
        min_index = min(min_index, i)
    return width