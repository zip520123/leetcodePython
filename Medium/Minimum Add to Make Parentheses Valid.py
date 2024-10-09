# Minimum Add to Make Parentheses Valid
# O(n), O(n)
def minAddToMakeValid(self, s: str) -> int:
    stack = []
    for char in s:
        if stack and stack[-1] == "(" and char == ")":
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

# O(n), O(1)
def minAddToMakeValid(self, s: str) -> int:
    open_brackets = 0
    min_required = 0
    for char in s:
        if char == "(":
            open_brackets += 1
        else:
            if open_brackets:
                open_brackets -= 1
            else:
                min_required += 1
    return open_brackets + min_required