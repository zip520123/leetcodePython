# Reconstruct Itinerary
# O(n log n), O(n)
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for (src, dst) in sorted(tickets, reverse = True):
        graph[src].append(dst)
    res = []
    def dfs(airport: str):
        while graph[airport]:
            dfs(graph[airport].pop())
        res.append(airport)
    dfs("JFK")
    return res[::-1]