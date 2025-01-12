# Zigzag Grid Traversal With Skip
# O(n), O(1)
def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
    res = []
    flag = True
    rows, cols = len(grid), len(grid[0])
    forward = True
    for row in range(rows):
        if forward:
            for col in range(cols):
                if flag:
                    res.append(grid[row][col])
                flag = not flag
        else:
            for col in range(cols-1, -1, -1):
                if flag:
                    res.append(grid[row][col])
                flag = not flag
        forward = not forward
    return res