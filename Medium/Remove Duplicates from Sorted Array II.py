# Remove Duplicates from Sorted Array II
# O(n), O(1)
def removeDuplicates(self, nums: List[int]) -> int:
    l, r = 0, 0
    count = 0
    prev = -math.inf
    while r<len(nums):
        if nums[r] == prev:
            count += 1
        else:
            count = 1
        prev = nums[r]
        if count > 2:
            while r<len(nums) and prev == nums[r]:
                r += 1
            if r<len(nums):
                prev = nums[r]
                count = 1
            if r==len(nums):
                break
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r += 1
    return l

# O(n), O(1)
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k