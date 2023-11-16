# Design Graph With Shortest Path Calculator
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(lambda: [])
        for currNode, nextNode, cost in edges:
            self.graph[currNode].append([nextNode,cost])

    def addEdge(self, edge: List[int]) -> None:
        currNode, nextNode, cost = edge
        self.graph[currNode].append([nextNode,cost])

    def shortestPath(self, node1: int, node2: int) -> int:
        seen = set()
        pq = [(0, node1)]
        while pq:
            currCost, currNode = heapq.heappop(pq)
            if currNode == node2: return currCost
            seen.add(currNode)
            for nextNode, nextCost in self.graph[currNode]:
                if nextNode not in seen:
                    heapq.heappush(pq, (currCost+nextCost, nextNode))
        return -1