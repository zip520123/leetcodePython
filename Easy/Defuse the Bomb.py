# Defuse the Bomb
# O(n*k), O(n)
def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0] * n
    if k == 0:
        return res
    for i in range(n):
        if k > 0:
            for j in range(1, k+1):
                res[i] += code[(i+j) % n]
        else:
            for j in range(k, 0, 1):
                res[i] += code[(i+j) % n]
    return res