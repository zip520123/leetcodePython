# Maximum Product Difference Between Two Pairs
# O(n log n), O(n)
def maxProductDifference(self, nums: List[int]) -> int:
    nums.sort(key=lambda x: x)
    return nums[-1] * nums[-2] - nums[0] * nums[1]