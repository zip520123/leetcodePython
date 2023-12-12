# Maximum Product of Two Elements in an Array
# O(n), O(1)
def maxProduct(self, nums: List[int]) -> int:
    a = nums[0]
    aIndex = 0
    n = len(nums)
    for i in range(1,n):
        if nums[i] > a:
            a = nums[i]
            aIndex = i
    b = 0
    for i in range(n):
        if nums[i] > b and i != aIndex:
            b = nums[i]
    return (a-1)*(b-1)