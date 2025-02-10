# Clear Digits
# O(n), O(n)
def clearDigits(self, s: str) -> str:
    res = []
    for char in s:
        if char.isdigit() and res:
            res.pop(-1)
        else:
            res.append(char)
    return "".join(res)