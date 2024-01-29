# Wiggle Sort
# O(n)
def wiggleSort(self, nums: List[int]) -> None:
    for i in range(1, len(nums)):
        if i%2 == 0:
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        else:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
