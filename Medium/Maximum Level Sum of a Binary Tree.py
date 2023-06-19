# Maximum Level Sum of a Binary Tree
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    if root == None: return 0
    maxlevel = 0
    currlevel = 0
    maxVal = -float('inf')
    queue = [root]
    while queue:
        temp = queue
        queue = []
        curr = 0
        currlevel += 1
        for node in temp:
            curr += node.val
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        if curr > maxVal:
            maxVal = curr
            maxlevel = currlevel
    return maxlevel