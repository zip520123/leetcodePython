# Minimum Number of Operations to Make Array Empty
# O(n), O(n)
def minOperations(self, nums: List[int]) -> int:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    res = 0
    for key, val in memo.items():
        if val == 1: return -1
        res += ceil(val/3)
    return res