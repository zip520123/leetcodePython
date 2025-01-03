# Number of Ways to Split Array
# O(n), O(n)
def waysToSplitArray(self, nums: List[int]) -> int:
    left_prefix = [0] * len(nums)
    right_prefix = [0] * len(nums)
    for i in range(len(nums)):
        left_prefix[i] += nums[i]
        if i > 0: 
            left_prefix[i] += left_prefix[i-1]
    for i in range(len(nums)-1, -1, -1):
        right_prefix[i] += nums[i]
        if i < len(nums)-1:
            right_prefix[i] += right_prefix[i+1]
    res = 0
    for i in range(1, len(nums)):
        if left_prefix[i-1] >= right_prefix[i]:
            res += 1
    return res

# O(n), O(1)
def waysToSplitArray(self, nums: List[int]) -> int:
    right_sum = sum(nums)
    res = 0
    left_sum = 0
    for i in range(len(nums)-1):
        left_sum += nums[i]
        right_sum -= nums[i]
        if left_sum >= right_sum:
            res += 1
    return res