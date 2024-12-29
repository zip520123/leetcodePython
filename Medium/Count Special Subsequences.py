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

