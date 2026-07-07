# Unique Middle Element
# O(n), O(1)
def isMiddleElementUnique(self, nums: list[int]) -> bool:
    mid_index = len(nums) // 2
    mid = nums[mid_index]
    count = 0
    for n in nums:
        if n == mid:
            count += 1
    return count == 1