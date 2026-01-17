# Largest Rectangle in Histogram
# O(n), O(n)
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    n = len(heights)
    res = 0
    for i in range(n):
        
        while stack and heights[stack[-1]] > heights[i]:
            last_idx = stack.pop()
            height = heights[last_idx]
            width = i
            if stack:
                width = i - stack[-1] - 1
            res = max(res, height * width)

        stack.append(i)

    while stack:
        last_idx = stack.pop()
        height = heights[last_idx]
        width = n
        if stack:
            width = n - stack[-1] - 1
        res = max(res, height * width)
    return res