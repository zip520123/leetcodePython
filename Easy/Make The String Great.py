# Make The String Great
# O(n), O(n)
def makeGood(self, s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1].lower() == char.lower():
            if stack[-1].isupper() and char.islower():
                stack.pop(-1)
            elif stack[-1].islower() and char.isupper():
                stack.pop(-1)
            else:
                stack.append(char)
        else:
            stack.append(char)
    return "".join(stack)