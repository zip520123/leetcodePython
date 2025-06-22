# Divide a String Into Groups of Size k
# O(n) time complexity, O(n) space complexity
def divideString(self, s: str, k: int, fill: str) -> List[str]:
    res = []
    index = 0
    curr = ""
    for char in s:
        curr += char
        if len(curr) == k:
            res.append(curr)
            curr = ""
    if len(curr) < k and curr != "":
        for _ in range(k-len(curr)):
            curr += fill
        res.append(curr)
    return res