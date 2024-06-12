# Sort Colors
# O(n), O(n)
def sortColors(self, nums: List[int]) -> None:
    res = []
    for n in nums:
        if n == 0:
            res.append(0)
    for n in nums:
        if n == 1:
            res.append(1)
    for n in nums:
        if n == 2:
            res.append(2)
    
    for i in range(len(res)):
        nums[i] = res[i]