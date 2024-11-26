# Find Champion II
# O(n), O(n)
def findChampion(self, n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(int)
    for a,b in edges:
        graph[b] += 1
    no_weaker_team = []
    for node in range(n):
        if graph[node] == 0:
            no_weaker_team.append(node)
    if len(no_weaker_team) > 1:
        return -1
    return no_weaker_team[0]