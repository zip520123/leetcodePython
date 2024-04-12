# Trapping Rain Water
# O(n), O(n)
def trap(self, height: List[int]) -> int:
    stack = []
    res = 0
    for i in range(len(height)):
        curr = height[i]
        while stack and height[stack[-1]] <= curr:
            prev_index = stack.pop(-1)
            prev = height[prev_index]
            if stack:
                res += (min(height[stack[-1]], curr) - prev) * (i-stack[-1]-1)
        stack.append(i)
    return res