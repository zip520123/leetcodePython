# Amount of Time for Binary Tree to Be Infected
# O(n), O(n)
def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    graph = defaultdict(list)
    q = []

    def dfs(node):
        if node == None: return
        if node.val == start:
            q.append(node)
        if node.left != None:
            graph[node].append(node.left)
            graph[node.left].append(node)
            dfs(node.left)
        if node.right != None:
            graph[node].append(node.right)
            graph[node.right].append(node)
            dfs(node.right)
    dfs(root)

    res = 0
    seen = set()
    seen.add(q[0])
    while q:
        temp = q
        q = []
        for node in temp:                
            for next_node in graph[node]:    
                if next_node not in seen:
                    seen.add(next_node)
                    q.append(next_node)
        res += 1
    return res - 1