# Decode String
# O(n), O(n)
def decodeString(self, s: str) -> str:
    curr_n = 0
    curr_s = ""
    stack = []
    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            curr_n = curr_n * 10 + int(char)
        elif char == "[":
            stack.append((curr_n, curr_s))
            curr_n = 0
            curr_s = ""
        elif char == "]":
            prev_n, prev_s = stack.pop(-1)
            curr_s = prev_s + curr_s * prev_n
        else:
            curr_s += char
    return curr_s