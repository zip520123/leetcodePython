# Frequency of the Most Frequent Element
# O(n log n), O(n)
def maxFrequency(self, nums: List[int], k: int) -> int:
    arr = sorted(nums)
    n = len(nums)
    l, r, res, curr = 0,0,0,0
    while r<n:
        target = arr[r]
        curr += arr[r]
        while (r-l+1)*target - curr > k:
            curr -= arr[l]
            l += 1
        res = max(res, r-l+1)
        r += 1
    return res