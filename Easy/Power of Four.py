# Power of Four
# O(log 4), O(1)
def isPowerOfFour(self, n: int) -> bool:
    if n == 1: return True
    p = 1
    while p < n:
        p *= 4
        if p == n: return True
    return False

# O(1), O(1)
def isPowerOfFour(self, n: int) -> bool:
    if n <= 0: return False
    a = math.log(n) / math.log(4)
    return a == int(a)