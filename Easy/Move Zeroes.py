# Move Zeroes
# O(n^2), O(1)
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    l = 0
    while l < n:
        if nums[l] == 0:
            i = l + 1
            while i < n and nums[i] == 0:
                i += 1
            if i == n:
                break
            nums[l], nums[i] = nums[i], nums[l]

        l += 1

# O(n), O(1)
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1