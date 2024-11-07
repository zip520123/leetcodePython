# Largest Combination With Bitwise AND Greater Than Zero
# O(n), O(n)
def largestCombination(self, candidates: List[int]) -> int:
    dp = [[0]*32 for _ in range(len(candidates))]
    for i in range(len(candidates)):
        num = candidates[i]
        for curr in range(32):
            dp[i][curr] = num & (2 ** curr)
    
    res = 0
    for i in range(32):
        curr = 0
        for j in range(len(candidates)):
            curr += 1 if dp[j][i] > 0 else 0
        res = max(res, curr)
    return res

# O(n), O(1)
def largestCombination(self, candidates: List[int]) -> int:
    res = 0
    for i in range(32):
        curr = 0
        for j in range(len(candidates)):
            curr += 1 if candidates[j] & (2 ** i) > 0 else 0
        res = max(res, curr)
    return res