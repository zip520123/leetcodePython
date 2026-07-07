# Single Number
# O(n), O(1)
def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    return res