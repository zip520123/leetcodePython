# Basic Calculator II
# O(n), O(n)
def calculate(self, s: str) -> int:
    sign = "+" 
    stack = []
    curr = 0

    for i in range(len(s)):
        char = s[i]
        if char == " ":
            continue
        if char in "+-*/":
            if sign == "+":
                stack.append(curr)
            if sign == "-":
                stack.append(-curr)
            if sign == "*":
                a = stack.pop(-1)
                stack.append(a*curr)
            if sign == "/":
                a = stack.pop(-1)
                stack.append(int(a/curr))
            sign = char
            curr = 0
        else:
            curr = curr * 10 + int(char)
    if sign == "+":
        stack.append(curr)
    if sign == "-":
        stack.append(-curr)
    if sign == "*":
        a = stack.pop(-1)
        stack.append(a*curr)
    if sign == "/":
        a = stack.pop(-1)
        stack.append(int(a/curr))
    
    return sum(stack)

# O(n), O(1)
def calculate(self, s: str) -> int:
    sign = "+" 
    last_val = 0
    curr = 0
    res = 0
    for i in range(len(s)):
        char = s[i]
        if char == " ":
            continue
        if char in "+-*/":
            if sign == "+":
                res += last_val
                last_val = curr
            if sign == "-":
                res += last_val
                last_val = -curr
            if sign == "*":
                last_val *= curr
            if sign == "/":
                last_val = int(last_val / curr)
            sign = char
            curr = 0
        else:
            curr = curr * 10 + int(char)
    if sign == "+":
        res += last_val
        last_val = curr
    if sign == "-":
        res += last_val
        last_val = -curr
    if sign == "*":
        last_val *= curr
    if sign == "/":
        last_val = int(last_val / curr)
    
    return res + last_val

# O(n), O(1)
def calculate(self, s: str) -> int:
    i = 0
    sign = "+"
    s += "+"
    m1, m2, res = 0, 0, 0
    
    for i in range(len(s)):
        curr = s[i]
        if curr == " ":
            continue
        if curr not in "+-*/":
            n = int(curr)
            m1 *= 10
            m1 += n
        else:
            if sign == "+":
                res += m2
                m2 = m1
                m1 = 0
            elif sign == "-":
                res += m2
                m2 = -m1
                m1 = 0
            elif sign == "*":
                m2 *= m1
                m1 = 0
            elif sign == "/":
                m2 = int(m2 / m1)
                m1 = 0
            sign = curr
    return res + m2