# Subarray Sum Equals K
# O(n), O(n)
def subarraySum(self, nums: List[int], k: int) -> int:
    memo = defaultdict(int)
    memo[0] = 1
    curr = 0
    res = 0
    for n in nums:
        curr += n
        res += memo[curr-k]
        memo[curr] += 1
    return res