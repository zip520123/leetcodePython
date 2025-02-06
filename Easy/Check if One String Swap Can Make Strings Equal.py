# Check if One String Swap Can Make Strings Equal
# O(n), O(1)
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    memo1 = defaultdict(int)
    for char in s1:
        memo1[char] += 1
    memo2 = defaultdict(int)
    for char in s2:
        memo2[char] += 1
    for i in range(ord("a"), ord("z")+1):
        if memo1[chr(i)] != memo2[chr(i)]:
            return False
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff <= 2