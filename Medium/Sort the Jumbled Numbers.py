# Sort the Jumbled Numbers
# O(n log n), O(n)
def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    memo = {}
    for i in range(len(nums)):
        n = nums[i]
        curr = mapping[nums[i] % 10]
        digits = 10
        n //= 10
        while n:
            digit = n % 10
            curr += mapping[digit] * digits
            digits *= 10
            n //= 10
        
        memo[nums[i]] = (curr, i)
    return sorted(nums, key= lambda x: memo[x])