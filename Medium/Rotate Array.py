# Rotate Array
# O(n), O(n)
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    t = n-k
    temp = nums + nums
    for i in range(n):
        nums[i] = temp[(i+t)%n]

# O(n), O(1)
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k%n
    l, r = 0, n-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = 0, k-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = k, n-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1