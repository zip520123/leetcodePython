# Sort an Array
# O(n log n), O(n)
def sortArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    if n <= 1: return nums
    left = self.sortArray(nums[:n//2])
    right = self.sortArray(nums[n//2:])
    res = []
    l, r = 0, 0
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    while l<len(left):
        res.append(left[l])
        l += 1
    while r<len(right):
        res.append(right[r])
        r += 1
    return res