# First Missing Positive
# O(n), O(n)
def firstMissingPositive(self, nums: List[int]) -> int:
    num_set = set(nums)
    for i in range(1, len(nums)+1):
        if i not in num_set:
            return i
    return len(nums)+1

# O(n), O(1)
def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n+1

    for num in nums:
        index = abs(num)-1
        if 0 <= index < n:
            nums[index] = -abs(nums[index])
    for i in range(n):
        if nums[i] > 0:
            return i+1
    return n+1
