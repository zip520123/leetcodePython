# Maximum Difference Between Node and Ancestor
# O(n), O(h)
def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    res = 0
    if root == None: return 0

    def dfs(node) -> (int, int):
        nonlocal res
        currMin, currMax = node.val, node.val
        if node.left != None:
            leftMin, leftMax = dfs(node.left)
            currMin = min(currMin, leftMin)
            currMax = max(currMax, leftMax)
            
        if node.right != None:
            rightMin, rightMax = dfs(node.right)
            currMin = min(currMin, rightMin)
            currMax = max(currMax, rightMax)

        res = max(res, abs(node.val - currMin), abs(node.val - currMax))
        return (currMin, currMax)
    dfs(root)
    return res