# Longest Square Streak in an Array
# O(n log n), O(n)
def longestSquareStreak(self, nums: List[int]) -> int:
    res = 0
    has = set(nums)
    seen = set()
    for n in nums:
        if n in seen:
            continue
        seen.add(n)
        curr = 1
        next_num = n * n
        while next_num in has:
            curr += 1
            seen.add(next_num)
            next_num *= next_num
        res = max(res, curr)
    if res <= 1:
        return -1
    return res