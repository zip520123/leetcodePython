# Open the Lock
# O(n), O(n)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        for deadend in deadends:
            seen.add(deadend)
        if "0000" in seen: 
            return -1
        queue = ["0000"]
        steps = 0
        while queue:
            temp = queue
            queue = []
            for node in temp:
                if node == target:
                    return steps
                for nextNode in Solution.nextNodes(node):
                    if nextNode not in seen:
                        seen.add(nextNode)
                        queue.append(nextNode)
            steps += 1
        return -1
    
    @staticmethod
    def nextNodes(node) -> List[str]:
        arr = []
        for i in range(4):
            curr = int(node[i])
            nextIncure = curr + 1
            if nextIncure == 10:
                nextIncure = 0
            nextDecure = curr - 1
            if nextDecure == -1:
                nextDecure = 9
            arr.append(node[:i] + str(nextIncure) + node[i+1:])
            arr.append(node[:i] + str(nextDecure) + node[i+1:])
        
        return arr