# Time Needed to Inform All Employees
# O(n), O(n)
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