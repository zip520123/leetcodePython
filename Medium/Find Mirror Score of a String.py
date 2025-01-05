# Find Mirror Score of a String
# O(n), O(n)
def calculateScore(self, s: str) -> int:
    memo = defaultdict(list)
    res = 0
    for i in range(len(s)):
        
        if len(memo[s[i]]) > 0:
            j = memo[s[i]].pop(-1)
            res += i-j
        else:
            asci = ord(s[i]) - ord("a")
            mirro_char = chr(25 - asci + ord("a"))
            memo[mirro_char].append(i)
    return res