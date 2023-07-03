# Buddy Strings
# O(n), O(1)
def buddyStrings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if s == goal:
        dp = defaultdict(int)
        for char in s:
            dp[char] += 1
            if dp[char] == 2:
                return True
        return False
    
    i1,i2 = -1,-1
    for i in range(len(s)):
        if s[i] != goal[i]:
            if i1 == -1:
                i1 = i
            elif i2 == -1:
                i2 = i
            else:
                return False
    if i2 == -1:
        return False

    return s[i1] == goal[i2] and s[i2] == goal[i1]