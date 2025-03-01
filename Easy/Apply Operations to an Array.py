# Apply Operations to an Array
# O(n), O(n)
def applyOperations(self, nums: List[int]) -> List[int]:
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:
            nums[l] *= 2
            nums[r] = 0
        l += 1
        r += 1
    res = [0] * len(nums)
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            res[l] = nums[r]
            l += 1
    return res
