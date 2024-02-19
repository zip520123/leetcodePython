# Power of Two
# O(1), O(1)
def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    curr = log(n, 2)
    
    return 2 ** int(curr) == n