# Evaluate Reverse Polish Notation
# O(n) time | O(n) space
def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t not in {"+", "-", "*", "/"}:
            stack.append(int(t))
        else:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if t == "+":
                stack.append(b+a)
            elif t == "-":
                stack.append(b-a)
            elif t == "*":
                stack.append(b*a)
            else:
                stack.append(int(b/a))
    
    return stack[0]