#  Count Subarrays Where Max Element Appears at Least K Times
# O(n), O(1)
def countSubarrays(self, nums: List[int], k: int) -> int:
    res = 0
    num = max(nums)
    n = len(nums)
    l = 0
    cnt = 0
    for r in range(n):
        if nums[r] == num:
            cnt += 1
        
        while cnt == k:
            res += n-r
            if nums[l] == num:
                cnt -= 1
            l += 1
    return res