# Make Sum Divisible by P
# O(n), O(n)
def minSubarray(self, nums: List[int], p: int) -> int:
    n = len(nums)
    total_sum = 0
    for num in nums:
        total_sum = (total_sum + num) % p

    remain = total_sum % p
    if remain == 0:
        return 0
    memo = {0:-1}
    curr = 0
    res = n
    
    for i in range(n):
        curr = (curr + nums[i]) % p
        needed = (curr - remain + p) % p
        if needed in memo:
            res = min(res, i - memo[needed]) 
        memo[curr] = i
    if res == n:
        return -1
    return res