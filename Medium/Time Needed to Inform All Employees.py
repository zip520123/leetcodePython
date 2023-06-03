# Time Needed to Inform All Employees
#DFS O(n), O(n)
def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    graph = collections.defaultdict(list)
    for i,m in enumerate(manager):
        graph[m].append(i)
    def dfs(node: int) -> int:
        time = 0
        for subNode in graph[node]:
            time = max(time, dfs(subNode))
        return time + informTime[node]

    return dfs(headID)

#BFS O(n),O(n)
def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    graph = collections.defaultdict(list)
    for i,m in enumerate(manager):
        graph[m].append(i)
    
    queue = [(headID, 0)]
    res = 0
    while queue:
        node, t = queue.pop()
        res = max(res, t)
        for subNode in graph[node]:
            queue.append((subNode, t+informTime[node]))
    return res
