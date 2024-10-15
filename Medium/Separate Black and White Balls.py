# Separate Black and White Balls
# O(n), O(1)
def minimumSteps(self, s: str) -> int:
    ones = 0
    res = 0
    for char in s:
        if char == "1":
            ones += 1
        else:
            res += ones
    return res