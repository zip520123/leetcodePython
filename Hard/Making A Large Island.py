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

# 
def largestIsland(self, grid: List[List[int]]) -> int:
    memo = {}
    def find(node):
        if node not in memo:
            memo[node] = node
        if memo[node] != node:
            memo[node] = find(memo[node])
        return memo[node]
    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        memo[root1] = root2
    
    rows, cols = len(grid), len(grid[0])
    dp = [[0]* cols for _ in range(rows) ]
    for row in range(rows):
        for col in range(cols):
            dp[row][col] = grid[row][col]
    res = 0
    roots_count = {}
    for row in range(rows):
        for col in range(cols):
            if dp[row][col] == 1:
                queue = [(row, col)]
                seen = set()
                
                while queue:
                    temp = queue
                    queue = []
                    for curr_row, curr_col in temp:
                        if (curr_row, curr_col) not in seen:
                            seen.add((curr_row, curr_col))
                            dp[curr_row][curr_col] = 0
                            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                                next_row, next_col = curr_row + dy, curr_col + dx
                                if 0 <= next_row < rows and 0 <= next_col < cols and dp[next_row][next_col] == 1:
                                    queue.append((next_row, next_col))

                for seen_row, seen_col in seen:
                    union((row, col), (seen_row, seen_col))
                roots_count[ find((row, col))] = len(seen)
                res = max(res, len(seen))
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                root_set = set()
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + dy, col + dx
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                        root_set.add(find((next_row, next_col)))
                curr = 1
                for root in root_set:
                    curr += roots_count[root]
                res = max(res, curr)
    return res