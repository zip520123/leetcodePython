# N-th Tribonacci Number
# O(n), O(1)
def tribonacci(self, n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    a, b, c = 0, 1, 1
    for _ in range(n-2):
        temp = a+b+c
        a = b
        b = c
        c = temp
    return c