# Minimize Length of Array Using Operations
# O(n log n), O(n)
def minimumArrayLength(self, nums: List[int]) -> int:
    arr = sorted(nums)
    n = len(nums)
    min_num = arr[0]
    for curr in nums[1:]:
        if curr % min_num != 0:
            return 1

    return (nums.count(min_num) + 1) // 2