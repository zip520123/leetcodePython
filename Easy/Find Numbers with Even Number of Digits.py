# Find Numbers with Even Number of Digits
# O(n), O(1)
def findNumbers(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        curr = n
        d = 0
        while curr:
            d += 1
            curr //= 10
        
        if d % 2 == 0:
            res += 1
    return res