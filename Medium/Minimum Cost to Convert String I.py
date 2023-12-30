# Minimum Cost to Convert String I
# O(source*changed), O(source*changed)
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for ori, nextNode, curr_cost in zip(original, changed, cost):
            heapq.heappush(graph[ori], (curr_cost, nextNode))
        
        arr = []
        for curr_char, target_char in zip(source, target):
            if curr_char != target_char: arr.append((curr_char, target_char))
        
        
        memo = {}

        def findCost(ori_char, target_char):
            if (ori_char, target_char) in memo: return memo[(ori_char, target_char)]
            queue = [(0, ori_char)]
            heapq.heapify(queue)
            seen = set()
            while queue:
                curr_cost, curr_char = heapq.heappop(queue)
                if curr_char == target_char:
                    memo[(ori_char, target_char)] = curr_cost
                    return curr_cost
                
                if curr_char not in seen:
                    seen.add(curr_char)
                    memo[(ori_char, curr_char)] = curr_cost
                    for next_cost, next_node in graph[curr_char]:
                        heapq.heappush(queue, (curr_cost+next_cost, next_node))
            return -1
            
        res = 0
        
        for (oriChar, targetChar) in arr:
            currCost = findCost(oriChar, targetChar)
            if currCost == -1: return -1
            res += currCost
        return res
                
            
        