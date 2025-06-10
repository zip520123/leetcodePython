# Maximum Difference Between Even and Odd Frequency I
# O(n), O(1)
def maxDifference(self, s: str) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    
    max_odd = 0
    max_even = math.inf
    for val in memo.values():
        if val % 2 == 0:
            max_even = min(max_even, val)
        else:
            max_odd = max(max_odd, val)
    
    return max_odd-max_even