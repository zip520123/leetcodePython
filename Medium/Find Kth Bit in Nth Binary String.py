# Find Kth Bit in Nth Binary String
# O(2^n), O(n)
def findKthBit(self, n: int, k: int) -> str:
    res = [0]
    for _ in range(n-1):
        temp = res
        res = res + [1] + list(map(lambda x: 0 if x == 1 else 1, reversed(temp)))
    return str(res[k-1])