# Minimize Length of Array Using Operations
# O(n log n), O(n)
def minimumArrayLength(self, nums: List[int]) -> int:
    min_num = min(nums)
    for n in nums:
        if n % min_num != 0: return 1
    return (nums.count(min_num) + 1) // 2