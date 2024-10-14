# Minimum Number of Swaps to Make the String Balanced
# O(n^2), O(n) TLE
def minSwaps(self, s: str) -> int:
    if s == "": return 0
    res = 0
    stack = []
    for char in s:
        if stack and stack[-1] == "[" and char == "]":
            stack.pop(-1)
        else:
            stack.append(char)
    if stack:
        res += 1
        stack[0], stack[-1] = stack[-1], stack[0]
        res += self.minSwaps("".join(stack))
    return res

# O(n), O(n)
def minSwaps(self, s: str) -> int:
    res = 0
    stack = []
    for char in s:
        if char == "[":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                res += 1

    return (res + 1) // 2