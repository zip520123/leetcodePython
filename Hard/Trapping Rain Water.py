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

# O(n), O(1)
def trap(self, height: List[int]) -> int:
    leftMax, rightMax = 0, 0
    l = 0
    r = len(height)-1
    res = 0
    while l<r:
        if height[l] < height[r]:
            if leftMax <= height[l]:
                leftMax = height[l]
            else:
                res += leftMax - height[l]
            l += 1
        else:
            if rightMax <= height[r]:
                rightMax = height[r]
            else:
                res += rightMax - height[r]
            r -= 1
    return res