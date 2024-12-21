# Maximum Number of K-Divisible Components
# O(n), O(n)
def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    res = 0
    seen = set()
    def dfs(node) -> int:
        nonlocal res
        if node in seen:
            return 0
        seen.add(node)
        
        sub_node_sum = 0
        for sub_node in graph[node]:
            sub_node_sum += dfs(sub_node)
        if (sub_node_sum + values[node]) % k == 0:
            res += 1
            
        return values[node] + sub_node_sum
    dfs(0)

    return res