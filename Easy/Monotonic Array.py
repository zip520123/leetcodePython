# Monotonic Array
# O(n), O(1)
def isMonotonic(self, nums: List[int]) -> bool:
    incre = True
    n = len(nums)
    for i in range(n-1):
        incre = incre and nums[i] <= nums[i+1]
    decre = True
    for i in range(n-1):
        decre = decre and nums[i] >= nums[i+1]
    return incre or decre