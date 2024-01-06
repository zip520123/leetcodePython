# Smallest Missing Integer Greater Than Sequential Prefix Sum
# O(n), O(n)
def missingInteger(self, nums: List[int]) -> int:
    numbers = set()
    for n in nums:
        numbers.add(n)
    curr = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - 1 != nums[i-1]:
            break
        curr += nums[i]
    while curr in numbers:
        curr += 1
    return curr