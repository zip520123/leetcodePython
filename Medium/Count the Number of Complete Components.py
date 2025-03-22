# Count the Number of Complete Components
# O(n), O(n)
def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    memo = {}
    def find(node) -> int:
        if node not in memo:
            memo[node] = node
        if memo[node] != node:
            memo[node] = find(memo[node])
        return memo[node]
    
    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        memo[root1] = root2


    node_links = defaultdict(int)
    for a,b in edges:
        node_links[a] += 1
        node_links[b] += 1
        union(a, b)
    
    components_count = defaultdict(int)
    for node in range(n):
        root = find(node)
        components_count[root] += 1
    
    complete_nodes = defaultdict(int)
    for node in range(n):
        root = find(node)
        curr_component_count = components_count[root]
        if curr_component_count-1 == node_links[node]:
            complete_nodes[root] += 1
    
    complete_root = set()
    for node in range(n):
        root = find(node)
        if complete_nodes[root] == components_count[root]:
            complete_root.add(root)
    return len(complete_root)