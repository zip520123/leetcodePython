# Rotate String
# O(s*goal), O(s)
def rotateString(self, s: str, goal: str) -> bool:
    if len(goal) < len(s):
        return False
    s += s
    for i in range(len(s)):
        found = False
        for j in range(len(goal)):
            if i+j < len(s) and s[i+j] == goal[j]:
                if j == len(goal) - 1:
                    found = True
            else:
                break
        if found:
            return True
    return False