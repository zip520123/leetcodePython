# Maximum Nesting Depth of the Parentheses
# O(n), O(1)
def maxDepth(self, s: str) -> int:
    res = 0
    count = 0
    for char in s:
        if char == "(":
            count += 1
            res = max(res, count)
        elif char == ")":
            count -= 1
    return res