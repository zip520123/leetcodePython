# Reduction Operations to Make the Array Elements Equal
# O(n log n), O(n)
def reductionOperations(self, nums: List[int]) -> int:
    nums.sort(reverse=True)
    res, count = 0,0

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            res += count
        count += 1
    return res