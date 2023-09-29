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
# O(n), O(1)
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        while i<j and nums[i] % 2 == 0:
            i += 1
        while i<j and nums[j] % 2 == 1:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums