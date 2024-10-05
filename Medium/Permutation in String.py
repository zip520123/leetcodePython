# Permutation in String
# O(n), O(n)
def checkInclusion(self, s1: str, s2: str) -> bool:
    memo = defaultdict(int)
    count = len(s1)
    for char in s1:
        memo[char] += 1
    
    l, r = 0, 0
    while r < len(s2):
        char = s2[r]
        memo[char] -= 1
        if memo[char] >= 0:
            count -= 1
            if count == 0:
                return True
        while memo[char] < 0:
            left_char = s2[l]
            memo[left_char] += 1
            if memo[left_char] > 0:
                count += 1
            l += 1
        r += 1
    return False  