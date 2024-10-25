# Longest Substring Without Repeating Characters
# O(n), O(n)
def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    res = 0
    l, r = 0, 0
    while r<len(s):
        char = s[r]
        if char not in char_set:
            char_set.add(char)
            res = max(res, len(char_set))
        else:
            while char in char_set and l < r:
                left_char = s[l]
                char_set.remove(left_char)
                l += 1
            char_set.add(char)
        r += 1
    return res

# O(n), O(n)
def lengthOfLongestSubstring(self, s: str) -> int:
    memo = defaultdict(int)
    res = 0
    l, r = 0, 0
    while r<len(s):
        char = s[r]
        memo[char] += 1
        while memo[char] > 1:
            left_char = s[l]
            memo[left_char] -= 1
            l += 1
        res = max(res, r-l+1)
        r += 1
    return res