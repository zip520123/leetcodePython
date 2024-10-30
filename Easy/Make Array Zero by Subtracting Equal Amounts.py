# Make Array Zero by Subtracting Equal Amounts
# O(n log n), O(n)
def minimumOperations(self, nums: List[int]) -> int:
    nums.sort()
    curr = 0
    res = 0
    for n in nums:
        if n > curr:
            curr = n
            res += 1
    return res