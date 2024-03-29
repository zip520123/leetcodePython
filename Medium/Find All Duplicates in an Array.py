# Find All Duplicates in an Array
# O(n), O(n)
def findDuplicates(self, nums: List[int]) -> List[int]:
    num_set = set()
    res = []
    for n in nums:
        if n in num_set:
            res.append(n)
        num_set.add(n)
    return res

# O(n), O(1)
def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            res.append(abs(nums[i]))
        nums[x] *= -1

    return res