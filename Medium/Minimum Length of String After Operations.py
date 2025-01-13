# Minimum Length of String After Operations
# O(n), O(1)
def minimumLength(self, s: str) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    res = 0
    for val in memo.values():
        curr = val
        while curr >= 3:
            curr -= 2
        res += curr
    return res

def minimumLength(self, s: str) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    res = 0
    for val in memo.values():
        if val % 2 == 1:
            res += 1
        else:
            res += 2
    return res