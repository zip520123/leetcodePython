# Minimum Number of Changes to Make Binary String Beautiful
# O(n), O(1)
def minChanges(self, s: str) -> int:
    stack = [s[0]]
    res = 0
    for i in range(1, len(s)):
        curr = s[i]
        if stack:
            last = stack.pop()
            if last != curr:
                res += 1
        else:
            stack.append(curr)
    return res

# O(n), O(1)
def minChanges(self, s: str) -> int:
    last = None
    res = 0
    for i in range(len(s)):
        curr = s[i]
        if last != None:
            if last != curr:
                res += 1
            last = None
        else:
            last = curr
    return res