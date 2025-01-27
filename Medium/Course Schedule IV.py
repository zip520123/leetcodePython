# Course Schedule IV
# O(n), O(n)
def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)
    memo = [ [False]* numCourses for _ in range(numCourses) ]

    for root in range(numCourses):
        queue = [root]
        seen = set()

        while queue:
            temp = queue
            queue = []
            for node in temp:
                if node not in seen:
                    memo[root][node] = True
                    seen.add(node)
                    for next_node in graph[node]:
                        queue.append(next_node)
    
    return [memo[a][b] for a,b in queries]