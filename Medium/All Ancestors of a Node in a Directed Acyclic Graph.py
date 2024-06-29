# All Ancestors of a Node in a Directed Acyclic Graph
# O(n), O(n)
def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node2].append(node1)

    @cache
    def dfs(node) -> List[int]:
        if len(graph[node]) == 0:
            return []
        curr = set()
        
        for ancesteor in graph[node]:
            curr.add(ancesteor)
            for ancesteors_ancesteor in dfs(ancesteor):
                curr.add(ancesteors_ancesteor)
        return sorted(curr)

    res = []
    for i in range(n):
        res.append(dfs(i))
    
    return res