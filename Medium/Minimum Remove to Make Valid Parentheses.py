# Minimum Remove to Make Valid Parentheses
# O(n), O(n)
def minRemoveToMakeValid(self, s: str) -> str:
    res = ""
    stack = []
    incorrect = set()
    for i in range(len(s)):
        char = s[i]
        if char == ")":
            if len(stack) == 0:
                incorrect.add(i)
            else:
                stack.pop(-1)
        if char == "(":
            stack.append(i)
    for i in stack:
        incorrect.add(i)
    for i in range(len(s)):
        if i not in incorrect:
            res += s[i]
    return res