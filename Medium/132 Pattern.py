# 132 Pattern
# O(n), O(n)
def find132pattern(self, nums: List[int]) -> bool:
    stack, third = [], float("-inf")
    for n in reversed(nums):
        if n < third: return True
        while stack and stack[-1] < n:
            third = stack.pop(-1)
        stack.append(n)
    return False