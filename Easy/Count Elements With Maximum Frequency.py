# Count Elements With Maximum Frequency
# O(n), O(n)
def maxFrequencyElements(self, nums: List[int]) -> int:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    maxFreq = 0
    for val in memo.values():
        maxFreq = max(maxFreq, val)
    res = 0
    for val in memo.values():
        if val == maxFreq:
            res += val
    return res