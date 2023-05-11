# Uncrossed Lines
# O(n*m) time, O(n*m) space
def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
    for i in range(1, len(nums1)+1 ):
        for j in range(1, len(nums2)+1 ):
            if nums1[i-1]==nums2[j-1]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(nums1)][len(nums2)]