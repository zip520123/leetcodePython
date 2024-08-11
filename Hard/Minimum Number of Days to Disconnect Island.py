# Minimum Number of Days to Disconnect Island
# O(n^2), O(n)
def minDays(self, grid: List[List[int]]) -> int:
    memo = {}
    rows, cols = len(grid), len(grid[0])
    islands = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                islands.append((row,col))
    
    def find(node: Tuple[int, int]) -> Tuple[int, int]:
        if node not in memo:
            memo[node] = node
            return node
        if memo[node] != node:
            memo[node] = find(memo[node])
        return memo[node]
    
    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        memo[root1] = root2
    for row in range(rows):
        for col in range(cols):
            if row+1 < rows and grid[row][col] == 1 and grid[row+1][col] == 1:
                union((row,col), (row+1,col))
            if col+1 < cols and grid[row][col] == 1 and grid[row][col+1] == 1:
                union((row,col), (row,col+1))
    roots = set()
    for island in islands:
        roots.add(find(island))
    
    if len(islands) == 1: return 1
    if len(roots) == 1 and len(islands) == 2: return 2
    if len(roots) >= 2 or len(roots) == 0: return 0

    for island_to_water in islands:
        memo = {}
        island_to_water_row, island_to_water_col = island_to_water
        grid[island_to_water_row][island_to_water_col] = 0
        for row in range(rows):
            for col in range(cols):
                if row+1 < rows and grid[row][col] == 1 and grid[row+1][col] == 1:
                    union((row,col), (row+1,col))
                if col+1 < cols and grid[row][col] == 1 and grid[row][col+1] == 1:
                    union((row,col), (row,col+1))
        new_roots = set()
        for island in islands:
            if island == island_to_water: continue
            new_roots.add(find(island))
        
        grid[island_to_water_row][island_to_water_col] = 1
        
        if len(new_roots) > len(roots): 
            return 1 
    return 2