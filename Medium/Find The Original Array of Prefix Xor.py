# Find The Original Array of Prefix Xor
# O(n), O(1)
def findArray(self, pref: List[int]) -> List[int]:
    res = [pref[0]]
    n = len(pref)
    for i in range(1,n):
        res.append(pref[i] ^ pref[i-1])
    return res

# O(n), O(1)
def findArray(self, pref: List[int]) -> List[int]:
    n = len(pref)
    for i in range(n-1,0,-1):
        pref[i] ^= pref[i-1]
    return pref