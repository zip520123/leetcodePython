# Lexicographical Numbers
# O(n), O(1)
def lexicalOrder(self, n: int) -> List[int]:
    res = []
    curr = 1
    for _ in range(n):
        res.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr >= n or curr % 10 == 9:
                curr //= 10
            curr += 1
    return res