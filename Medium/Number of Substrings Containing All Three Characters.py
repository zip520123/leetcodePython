# Number of Substrings Containing All Three Characters
# O(n), O(1)
def numberOfSubstrings(self, s: str) -> int:
    l, r, total = 0, 0, 0
    freq = defaultdict(int)
    while r < len(s):
        freq[s[r]] += 1
        while freq["a"] > 0 and freq["b"] > 0 and freq["c"] > 0:
            total += len(s) - r
            freq[s[l]] -= 1
            l += 1
        r += 1
    return total