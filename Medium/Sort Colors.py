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
# O(n), O(1)
def sortColors(self, nums: List[int]) -> None:
    i, l, r = 0, 0, len(nums)-1
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
            l += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1