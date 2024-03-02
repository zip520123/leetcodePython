# Squares of a Sorted Array
# O(n), O(1)
def sortedSquares(self, nums: List[int]) -> List[int]:
    res = []
    l, r = 0, len(nums)-1
    while l<=r:
        left = nums[l] * nums[l]
        right = nums[r] * nums[r]
        if left < right:
            res.append(right)
            r -= 1
        else:
            res.append(left)
            l += 1
    return reversed(res)
    