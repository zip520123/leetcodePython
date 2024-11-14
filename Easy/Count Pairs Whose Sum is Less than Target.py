# Count Pairs Whose Sum is Less than Target
# O(n^2), O(1)
def countPairs(self, nums: List[int], target: int) -> int:
    res = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] < target:
                res += 1
    return res