# Missing Number
# O(n), O(1)
def missingNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    for n in range(len(nums)+1):
        res = res ^ n
    return res

# O(n), O(1)
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    res = (1+n) * n // 2
    for num in nums:
        res -= num
    return res