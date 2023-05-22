# Evaluate Division
# O(n) time, O(n) space
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set); chars = set(); wei = {}
        for (a,b), val in zip(equations, values):
            chars.add(a)
            chars.add(b)
            graph[a].add(b)
            graph[b].add(a)
            wei[a+"->"+b] = val
            wei[b+"->"+a] = 1/val

        def calc(que: List[str]) -> float:
            start = que[0]; end = que[1]
            if start == end and start in chars:
                return 1
            seen = set()
            queue = [(start, 1)]
            while len(queue) > 0:
                a, prevWei = queue.pop()
                for next in graph[a]:
                    if next in seen:
                        continue

                    currWei = wei[a+"->"+next] * prevWei
                    if next == end:
                        return currWei

                    seen.add(next)
                    queue.append((next, currWei))
            return -1

        return map(calc, queries)

# 
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = collections.defaultdict(dict)
    for (a,b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1/val

    def calc(que: List[str]) -> float:
        start = que[0]; end = que[1]
        if not (start in graph and end in graph): return -1
            
        seen = set()
        queue = [(start, 1)]
        while len(queue) > 0:
            curr, val = queue.pop()
            if curr == end:
                return val

            seen.add(curr)
            for next in graph[curr]:
                if next not in seen:
                    queue.append((next,val*graph[curr][next]))
        return -1

    return [calc(que) for que in queries]