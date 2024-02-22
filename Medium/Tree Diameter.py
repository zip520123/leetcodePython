# Tree Diameter
# O(n), O(n)
def treeDiameter(self, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    q = [0]
    seen = set()
    prev = None
    while q:
        temp = q
        q = []
        for node in temp:
            if node in seen: continue
            seen.add(node)
            prev = node
            for nextNode in graph[node]:
                q.append(nextNode)
    q = [prev]
    seen = set()
    c = None
    while q:
        temp = q
        q = []
        for node in temp:
            if node in seen: continue
            seen.add(node)
            c = node
            for nextNode in graph[node]:
                q.append(nextNode)
    res = 0
    q = [prev]
    seen = set()
    while q:
        res += 1
        temp = q
        q = []
        for node in temp:
            if node in seen: continue
            seen.add(node)

            for nextNode in graph[node]:
                if nextNode == c:
                    return res
                q.append(nextNode)
    return 0

# O(n), O(n)
def treeDiameter(self, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(node) -> int:
        q = [node]
        seen = set()
        prev = None
        while q:
            temp = q
            q = []
            for node in temp:
                if node in seen: continue
                seen.add(node)
                prev = node
                for nextNode in graph[node]:
                    q.append(nextNode)
        return prev
    a = bfs(0)
    b = bfs(a)
    res = 0
    q = [a]
    seen = set()
    while q:
        res += 1
        temp = q
        q = []
        for node in temp:
            if node in seen: continue
            seen.add(node)
            for nextNode in graph[node]:
                if nextNode == b:
                    return res
                q.append(nextNode)
    return 0