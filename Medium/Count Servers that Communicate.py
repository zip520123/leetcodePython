# Count Servers that Communicate
# O(n), O(n)
def countServers(self, grid: List[List[int]]) -> int:
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
    for row in range(rows):
        arr = []
        for col in range(cols):
            if grid[row][col]:
                arr.append(col)
        
        for i in range(1, len(arr)):
            node1 = (row, arr[i - 1])
            node2 = (row, arr[i])
            union(node1, node2)
    
    for col in range(cols):
        arr = []
        for row in range(rows):
            if grid[row][col]:
                arr.append(row)
        for i in range(1, len(arr)):
            node1 = (arr[i-1], col)
            node2 = (arr[i], col)
            union(node1, node2)
    
    roots_count = defaultdict(int)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                root = find((row, col))
                roots_count[root] += 1
    
    res = 0
    for count in roots_count.values():
        if count > 1:
            res += count
    
    return res