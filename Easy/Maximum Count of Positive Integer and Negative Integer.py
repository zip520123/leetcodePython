# Maximum Count of Positive Integer and Negative Integer
# O(n), O(1)
def maximumCount(self, nums: List[int]) -> int:
    pos, neg = 0, 0
    for n in nums:
        if n > 0:
            pos += 1
        if n < 0:
            neg += 1
    return max(pos, neg)