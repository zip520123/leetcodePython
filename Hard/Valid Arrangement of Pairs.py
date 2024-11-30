# Valid Arrangement of Pairs
# O(n), O(n)
def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
    graph = defaultdict(list)
    in_count = defaultdict(int)
    out_count = defaultdict(int)

    for a, b in pairs:
        graph[a].append(b)
        in_count[a] += 1
        out_count[b] += 1
    
    start = -1
    for node, count in in_count.items():
        if out_count[node] < count:
            start = node
            break
    if start == -1:
        start = pairs[0][0]
    
    arr = []

    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        arr.append(node)
    
    dfs(start)
    arr.reverse()

    return [ [arr[i-1],arr[i]] for i in range(1, len(arr))]