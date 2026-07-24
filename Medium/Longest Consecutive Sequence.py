# Longest Consecutive Sequence
# O(n) time | O(n) space
def longestConsecutive(self, nums: List[int]) -> int:
    set1 = set(nums)
    res = 0
    for n in set1:
        if n - 1 not in set1:
            curr = 1
            while n + 1 in set1:
                curr += 1
                n += 1
            res = max(res, curr)
    return res