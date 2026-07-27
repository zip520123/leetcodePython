# Maximum Sum Circular Subarray
# O(n),O(1)
def maxSubarraySumCircular(self, nums: List[int]) -> int:
    maxSum = currSum = nums[0]
    for n in nums[1:]:
        currSum = max(n, currSum+n)
        maxSum = max(maxSum, currSum)
    if maxSum < 0:
        return maxSum
    minSum = currSum = nums[0]
    for n in nums[1:]:
        currSum = min(n, currSum+n)
        minSum = min(minSum, currSum)
    total = sum(nums)
    return max(total - minSum, maxSum)