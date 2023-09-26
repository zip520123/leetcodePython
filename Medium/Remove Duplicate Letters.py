# Remove Duplicate Letters
# O(n), O(n)
def removeDuplicateLetters(self, s: str) -> str:
    count = defaultdict(int)
    
    for char in s:
        count[char] += 1
    has = defaultdict(lambda: False)
    stack = []
    for char in s:
        count[char] -= 1
        if has[char]: continue
        while stack and stack[-1] > char and count[stack[-1]] > 0:
            has[stack[-1]] = False
            stack.pop(-1)
        stack.append(char)
        has[char] = True
    return "".join(stack)