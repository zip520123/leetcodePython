# Maximum Score From Removing Substrings
# O(n), O(n)
def maximumGain(self, s: str, x: int, y: int) -> int:
    
    def caculate(char1, char2, x, y) -> int:
        stack = []
        res = 0
        for char in s:
            if stack and stack[-1] == char1 and char == char2:
                res += x
                stack.pop(-1)
            else:
                stack.append(char)
        stack2 = []
        for char in stack:
            if stack2 and stack2[-1] == char2 and char == char1:
                res += y
                stack2.pop(-1)
            else:
                stack2.append(char)
        return res
    return max(caculate("a", "b", x, y), caculate("b", "a", y, x))