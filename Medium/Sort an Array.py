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

# O(n), O(1)
def sortArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    counting = [0 for _ in range(-5 * 10 ** 4, 5 * 10 ** 4 + 1)]
    for n in nums:
        counting[n+5 * 10 ** 4] += 1
    res = []
    for i in range(len(counting)):
        freq = counting[i]
        n = i - 5 * 10 ** 4
        for _ in range(freq):
            res.append(n)
    return res