# Max Consecutive Ones III
# O(n), O(1)
def longestOnes(self, nums: List[int], k: int) -> int:
    count = 0
    used = 0
    res = 0
    l, r = 0, 0
    while r < len(nums):
        if nums[r] == 1:
            count += 1
        else:
            used += 1
            count += 1
            while used > k:
                count -= 1
                if nums[l] == 0:
                    used -= 1
                l += 1
        res = max(res, count)

        r += 1
    return res