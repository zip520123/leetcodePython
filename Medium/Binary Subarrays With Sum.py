# Binary Subarrays With Sum
# O(n), O(n)
def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    memo = defaultdict(int)
    memo[0] = 1
    res = 0
    prefix_sum = 0
    for n in nums:
        prefix_sum += n
        res += memo[prefix_sum-goal]
        memo[prefix_sum] += 1
    return res