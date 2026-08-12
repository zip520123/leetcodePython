# Max Number of K-Sum Pairs
# O(n), O(n)
def maxOperations(self, nums: List[int], k: int) -> int:
    memo = {}
    for n in nums:
        if n not in memo:
            memo[n] = 0
        memo[n] += 1
    res = 0
    for key in memo.keys():
        a = key
        b = k-a
        if b not in memo:
            continue
        if a == b:
            res += memo[a] // 2
        else:
            t = min(memo[a], memo[b])
            res += t
            memo[a] -= t
            memo[b] -= t
    return res