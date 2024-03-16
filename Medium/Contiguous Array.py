# Contiguous Array
# O(n), O(n)
def findMaxLength(self, nums: List[int]) -> int:
    prefix_sum = 0
    memo = {0:-1}
    
    res = 0
    for i in range(len(nums)):
        n = nums[i]
        
        if n == 1:
            prefix_sum += 1
        else:
            prefix_sum -= 1
        
        if prefix_sum in memo:
            res = max(res, i-memo[prefix_sum])
        else:
            memo[prefix_sum] = i
    return res