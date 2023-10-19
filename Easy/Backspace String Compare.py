# Backspace String Compare
# O(n), O(n)
def backspaceCompare(self, s: str, t: str) -> bool:

    def process(s) -> [str]:
        stack = []
        for char in s:
            if char == "#":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(char)
        return stack

    return process(s) == process(t)

# O(n), O(1)
def backspaceCompare(self, s: str, t: str) -> bool:
    l, r = len(s)-1, len(t)-1
    d1, d2 = 0, 0
    while l>=0 or r>=0:
        while l>=0:
            if s[l] == "#":
                d1 += 1
                l -= 1
            elif d1 > 0:
                l -= 1
            else:
                break
        while r>=0:
            if t[r] == "#":
                d2 += 1
                r -= 1
            elif d2 > 0:
                r -= 1
            else:
                break
        if l == -1 and r == -1: return True
        if l == -1 or r == -1: return False
        if s[l] != t[r]: return False
        l -= 1
        r -= 1

    return l == -1 and r == -1
