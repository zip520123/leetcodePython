# Clone Graph
# O(n), O(n)
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if node == None: 
        return None
    
    clone = defaultdict(list)
    def dfs(curr):
        nonlocal clone
        if curr.val not in clone:
            newNode = Node(curr.val, [])
            clone[curr.val] = newNode
            for nei in curr.neighbors:
                dfs(nei)
                newNode.neighbors.append(clone[nei.val])
        
    dfs(node)
    return clone[node.val]