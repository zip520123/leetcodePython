# Count Nodes Equal to Average of Subtree
# O(n), O(n)
class NodeInfo(NamedTuple):
    subnodeCount: int
    sum: int
    resCount: int
    
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node) -> NodeInfo:
            if node == None: return NodeInfo(0,0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            currCount = left.subnodeCount + right.subnodeCount + 1
            currSum = left.sum + right.sum + node.val
            resCount = left.resCount + right.resCount 
            if currSum // currCount == node.val: resCount += 1
            return NodeInfo(currCount, currSum, resCount)
        
        return dfs(root).resCount