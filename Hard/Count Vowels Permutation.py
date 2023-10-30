# Count Vowels Permutation
# O(n), O(1)
def countVowelPermutation(self, n: int) -> int:
    a = e = i = o = u = 1
    mod = 1E9+7
    for _ in range(1, n):
        newA = (e+i+u) % mod
        newE = (a+i) % mod
        newI = (e+o) % mod
        newO = i % mod
        newU = (i+o) % mod
        a, e, i, o, u = newA, newE, newI, newO, newU
    return int((a+e+i+o+u) % mod)