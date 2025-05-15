# Longest Unequal Adjacent Groups Subsequence I
# O(n), O(n)
def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    n = len(words)
    stack = []
    for i in range(n):
        if stack:
            if groups[stack[-1]] != groups[i]:
                stack.append(i)
        else:
            stack.append(i)
    return [ words[i] for i in stack ]