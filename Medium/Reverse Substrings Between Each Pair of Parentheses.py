# Reverse Substrings Between Each Pair of Parentheses
# O(n), O(n)
def reverseParentheses(self, s: str) -> str:
    stack = []
    for char in s:
        if char == ")":
            queue = []
            while stack and stack[-1] != "(":
                curr = stack.pop(-1)
                queue.append(curr)
            if stack[-1] == "(":
                stack.pop(-1)
            stack += queue
                
        else:
            stack.append(char)
    
    return "".join(stack)