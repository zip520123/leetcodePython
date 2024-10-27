# Longest Common Prefix
# O(n), O(n)
def longestCommonPrefix(self, strs: List[str]) -> str:
    min_str_count = math.inf
    for s in strs:
        min_str_count = min(min_str_count, len(s))
    word = ""
    for s in strs:
        if len(s) == min_str_count:
            word = s
    res = ""
    for i in range(min_str_count):
        for s in strs:
            if word[i] != s[i]:
                return res
        res += word[i]
    return res