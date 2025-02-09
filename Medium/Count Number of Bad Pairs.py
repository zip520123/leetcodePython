# Count Number of Bad Pairs
# O(n), O(n)
def countBadPairs(self, nums: List[int]) -> int:
    n = len(nums)
    memo = defaultdict(int)
    for i in range(n):
        memo[nums[i] - i] += 1
    res = (n - 1 + 1) * (n - 1) // 2
    for val in memo.values():
        res -= (val - 1 + 1) * (val - 1) // 2
    return res