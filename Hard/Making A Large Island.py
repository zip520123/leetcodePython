# Making A Large Island
# O(n log n), O(n)
def largestIsland(self, grid: List[List[int]]) -> int:
    memo = {}
    def find(x, y) -> (int,int):
        if (x,y) not in memo:
            memo[(x,y)] = (x,y)
            return memo[(x,y)]
        if memo[(x,y)] != (x,y):
            rootX, rootY = memo[(x,y)]
            memo[(x,y)] = find(rootX, rootY)
        return memo[(x,y)]
    def union(x1, y1, x2, y2):
        root1, root2 = find(x1,y1), find(x2,y2)
        memo[root2] = root1
    rows, cols = len(grid), len(grid[0])
    seen = set()
        
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in seen:
                root = find(row,col)
                queue = [(row,col)]
                seen.add(root)
                while queue:
                    temp = queue
                    queue = []
                    for node in temp:
                        union(root[0], root[1], node[0], node[1])
                        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                            nextX = node[0] + dx
                            nextY = node[1] + dy
                            if 0 <= nextX < rows and \
                                0 <= nextY < cols and \
                                grid[nextX][nextY] == 1 and \
                                (nextX, nextY) not in seen:
                                seen.add((nextX, nextY))
                                queue.append((nextX, nextY))
    rootToCount = defaultdict(int)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                root = find(row,col)
                rootToCount[root] += 1

    res = 1
    for root, val in rootToCount.items():
        res = max(res, val)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                landsRoots = set()
                for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nextX = row + dx
                    nextY = col + dy
                    if 0 <= nextX < rows and \
                        0 <= nextY < cols and \
                        grid[nextX][nextY] == 1:
                        root = find(nextX, nextY)
                        landsRoots.add((root[0], root[1]))
                curr = 1
                for root in landsRoots:
                    curr += rootToCount[root]
                res = max(res, curr)
    return res