# Minimum Number of Operations to Move All Balls to Each Box
# O(n^2) time O(n^2) space
def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    dp = [ [0] * n for _ in range(n)]
    for i in range(n):
        char = boxes[i]
        if char == "1":
            for j in range(i-1, -1, -1):
                dp[i][j] = dp[i][j+1] + 1
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] + 1
    res = [0] * n
    for col in range(n):
        for row in range(n):
            res[col] += dp[row][col]
    return res

# O(n), O(n) space
def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    dp_left = [0] * n
    for i in range(1, n):
        dp_left[i] += dp_left[i-1]
        if boxes[i-1] == "1":
            dp_left[i] += 1
    for i in range(1, n):
        dp_left[i] += dp_left[i-1]
    
    dp_right = [0] * n
    for i in range(n-2, -1, -1):
        dp_right[i] += dp_right[i+1]
        if boxes[i+1] == "1":
            dp_right[i] += 1
    for i in range(n-2, -1, -1):
        dp_right[i] += dp_right[i+1]
    res = [0] * n
    for i in range(n):
        res[i] = dp_left[i] + dp_right[i]
    
    return res  