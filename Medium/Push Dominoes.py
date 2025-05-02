# Push Dominoes
# O(n), O(n)
def pushDominoes(self, dominoes: str) -> str:
    stack = []
    res = ""
    for char in dominoes:
        if char == ".":
            stack.append(char)
        elif char == "L":
            if stack:
                stack.append(char)
                if stack[0] == ".":
                    res += "L" * len(stack)
                elif stack and stack[0] == "R":
                    res += "R" * (len(stack) // 2)
                    if len(stack) % 2 == 1:
                        res += "."
                    res += "L" * (len(stack) // 2)
                stack = []
            else:
                res += "L"

        elif char == "R":
            if stack and stack[0] == "R":
                res += "R" * len(stack)
            else:
                for el in stack:
                    res += el
            stack = []
            stack.append(char)
        
    if stack and stack[0] == "R":
        res += "R" * len(stack)
    else:
        for char in stack:
            res += char
    return res