# Find Polygon With the Largest Perimeter
# O(n log n), O(n)
def largestPerimeter(self, nums: List[int]) -> int:
    res = -1
    nums.sort()
    curr = nums[0] + nums[1]
    for i in range(2, len(nums)):
        n = nums[i]
        if curr > n:
            res = max(res, curr+n)
        curr += n
    return res