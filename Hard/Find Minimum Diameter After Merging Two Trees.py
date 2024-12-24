# Find Minimum Diameter After Merging Two Trees
def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
    graph1 = defaultdict(list)
    for a, b in edges1:
        graph1[a].append(b)
        graph1[b].append(a)
    graph2 = defaultdict(list)
    for a, b in edges2:
        graph2[a].append(b)
        graph2[b].append(a)
    d1, d2 = self.bfs_diameter(graph1), self.bfs_diameter(graph2)

    return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)

def bfs_diameter(self, graph) -> int:
    queue = [0]
    seen = set()
    seen.add(0)
    
    last_node = 0
    while queue:
        temp = queue
        queue = []
        for node in temp:
            last_node = node
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    queue.append(next_node)
    level = 0
    queue = [last_node]
    seen = set()
    seen.add(last_node)
    while queue:
        temp = queue
        queue = []
        for node in temp:
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    queue.append(next_node)
        if queue:
            level += 1
    
    return level