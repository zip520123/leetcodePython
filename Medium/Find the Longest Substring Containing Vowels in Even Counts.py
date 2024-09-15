# Find the Longest Substring Containing Vowels in Even Counts
# O(n), O(1)
def findTheLongestSubstring(self, s: str) -> int:
    res = 0
    curr_mask = 0
    vowels = { "a": 1, "e": 2, "i": 4, "o": 8, "u": 16 }
    mask_index = { 0: -1 }
    for i in range(len(s)):
        curr_mask ^= vowels.get(s[i], 0)
        if curr_mask in mask_index:
            res = max(res, i - mask_index[curr_mask])
        else:
            mask_index[curr_mask] = i
    return res