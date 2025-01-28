# Maximum Number of Fish in a Grid
# O(n), O(n)
def findMaxFish(self, grid: List[List[int]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0:
                queue = [(row, col)]
                curr = 0
                while queue:
                    temp = queue
                    queue = []
                    for curr_row, curr_col in temp:
                        curr += grid[curr_row][curr_col]
                        
                        grid[curr_row][curr_col] = 0
                        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            next_col, next_row = curr_col + dx, curr_row + dy
                            if 0 <= next_col < cols and 0 <= next_row < rows and grid[next_row][next_col]:
                                queue.append((next_row, next_col))
                res = max(res, curr)
    return res

# O(n), O(n) union find
def findMaxFish(self, grid: List[List[int]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])
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
    

    for row in range(rows):
        curr_root = None
        for col in range(cols):
            if grid[row][col] > 0:
                if curr_root == None:
                    curr_root = (row, col)
                else:
                    union(curr_root, (row, col))
            else:
                curr_root = None

    for col in range(cols):
        curr_root = None
        for row in range(rows):
            if grid[row][col] > 0:
                if curr_root == None:
                    curr_root = (row, col)
                else:
                    union(curr_root, (row, col))
            else:
                curr_root = None

    node_to_roots = defaultdict(int)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0:
                curr_root = find((row, col))
                node_to_roots[curr_root] += grid[row][col]
    res = 0
    for val in node_to_roots.values():
        res = max(res, val)
    return res