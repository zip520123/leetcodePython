# Make String a Subsequence Using Cyclic Increments
# O(n), O(1)
def canMakeSubsequence(self, str1: str, str2: str) -> bool:
    cyclically = {}
    for asci_num in range(ord("a"), ord("z")+1):
        char = chr(asci_num)
        next_char = chr(((asci_num + 1 - ord("a")) % 26) + ord("a"))
        cyclically[char] = next_char
    l, r = 0, 0
    while l < len(str1) and r < len(str2):
        if str1[l] == str2[r] or cyclically[str1[l]] == str2[r]:
            r += 1
        l += 1

    return r == len(str2)