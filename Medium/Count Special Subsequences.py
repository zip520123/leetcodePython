# Count Special Subsequences
# O(n^4), O(n), TLE
def numberOfSubsequences(self, nums: List[int]) -> int:
    res = 0
    for p in range(len(nums)-3):
        for q in range(p+2, len(nums)-2):
            for r in range(q+2, len(nums)-1):
                for s in range(r+2, len(nums)):
                    if nums[p] * nums[r] == nums[q] * nums[s]:
                        res += 1
    return res

# Count Special Subsequences
# O(n^2), O(n)
def numberOfSubsequences(self, nums: List[int]) -> int:
    res = 0
    memo = defaultdict(int)
    for r in range(4, len(nums)-2):
        q = r - 2
        for p in range(q-1):
            key = nums[p]/nums[q]
            memo[key] += 1
        for s in range(r + 2, len(nums)):
            res += memo[nums[s]/nums[r]]

    return res