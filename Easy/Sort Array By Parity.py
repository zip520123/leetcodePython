# Sort Array By Parity
# O(n), O(n)
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        if n%2 == 0:
            res.insert(0, n)
        else:
            res.append(n)
    return res