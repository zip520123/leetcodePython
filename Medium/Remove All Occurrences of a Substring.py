# Remove All Occurrences of a Substring
# O(n), O(n)
def removeOccurrences(self, s: str, part: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= len(part) and "".join(stack[len(stack)-len(part):len(stack)]) == part:
            stack = stack[:len(stack)-len(part)]
    return "".join(stack)

def removeOccurrences(self, s: str, part: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= len(part) and "".join(stack[-len(part):]) == part:
            stack = stack[:-len(part)]
    return "".join(stack)