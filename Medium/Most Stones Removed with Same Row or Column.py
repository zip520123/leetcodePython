# Most Stones Removed with Same Row or Column
# O(n^2), O(n)
def removeStones(self, stones: List[List[int]]) -> int:
    rows, cols = 0, 0
    for x,y in stones:
        rows = max(rows, x)
        cols = max(cols, y)
    
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
    
    for row in range(rows+1):
        nodes = []
        for stone in stones:
            if stone[0] == row:
                nodes.append(stone)
        for i in range(len(nodes)-1):
            node1 = (nodes[i][0], nodes[i][1])
            node2 = (nodes[i+1][0], nodes[i+1][1])
            union(node1, node2)
    
    for col in range(cols+1):
        nodes = []
        for stone in stones:
            if stone[1] == col:
                nodes.append(stone)
        for i in range(len(nodes)-1):
            node1 = (nodes[i][0], nodes[i][1])
            node2 = (nodes[i+1][0], nodes[i+1][1])
            union(node1, node2)
    res = 0
    for stone in stones:
        node = (stone[0], stone[1])
        root = find(node)
        if root != node:
            res += 1
    return res

# O(n), O(n)
def removeStones(self, stones: List[List[int]]) -> int:
    count = 0
    memo = {}
    def find(p: int) -> int:
        nonlocal count
        if p not in memo:
            count += 1
            memo[p] = p
        if memo[p] != p:
            memo[p] = find(memo[p])
        return memo[p]
    def union(p1, p2):
        nonlocal count
        root1, root2 = find(p1), find(p2)
        if root1 != root2:
            count -= 1
        memo[root1] = root2
    
    for stone in stones:
        union(stone[0], ~stone[1])
    return len(stones) - count