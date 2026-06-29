# Edit Distance
# O(word1*word2), O(word1*word2)
def minDistance(self, word1: str, word2: str) -> int:
    cols, rows = len(word1), len(word2)
    dp = [[0] * (cols + 1) for _ in range(rows+1)]
    for i in range(1, cols+1):
        dp[0][i] = i
    for i in range(1, rows+1):
        dp[i][0] = i
    
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if word2[i-1] == word1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[rows][cols]