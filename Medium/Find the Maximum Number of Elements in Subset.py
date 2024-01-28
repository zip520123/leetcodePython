# Find the Maximum Number of Elements in Subset
# O(n log n), O(n)
def maximumLength(self, nums: List[int]) -> int:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    curr = memo[1]
    if curr % 2 == 0: curr -= 1
    res = 1
    res = max(res, curr)
    nums.sort()
    for base in nums:
        if base > 1:
            curr_base = base
            curr = 1
            while memo[curr_base] > 1 and memo[curr_base*curr_base] > 0:
                curr += 2
                memo[curr_base] = 0
                curr_base *= curr_base
            res = max(res, curr)
    return res