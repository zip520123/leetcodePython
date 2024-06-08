# Continuous Subarray Sum
# O(n), O(n)
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    sum = 0
    memo = {0:-1}
    for i in range(len(nums)):
        n = nums[i]
        sum += n
        if sum % k in memo:
            if i-memo[sum%k] > 1:
                return True
        else:
            memo[sum%k] = i
    return False