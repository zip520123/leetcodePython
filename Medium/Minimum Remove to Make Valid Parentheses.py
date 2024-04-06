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

# O(n), O(n)
def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    for i in range(len(s)):
        char = s[i]
        if char == ")":
            if stack and stack[-1][0] == "(":
                stack.pop(-1)
            else:
                stack.append((char, i))
        elif char == "(":
            stack.append((char, i))
    
    res = ""
    for i in range(len(s)):
        char = s[i]
        if stack and stack[0][1] == i:
            stack.pop(0)
        else:
            res += char
    return res