# Buildings With an Ocean View
# O(n), O(n)
def findBuildings(self, heights: List[int]) -> List[int]:
    stack = []
    for i in range(len(heights)):
        h = heights[i]
        while stack and heights[stack[-1]] <= h:
            stack.pop(-1)
        stack.append(i)
    return stack