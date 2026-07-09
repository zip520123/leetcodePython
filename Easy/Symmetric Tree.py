# Symmetric Tree
# O(n), O(n)
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root == None: 
        return True
    l = [root.left]
    r = [root.right]
    while l or r:
        if len(l) != len(r):
            return False
        n = len(l)
        for _ in range(n):
            leftNode = l.pop(0)
            rightNode = r.pop(0)
            
            if leftNode == None and rightNode != None:
                return False
            if leftNode != None and rightNode == None:
                return False
            if leftNode == None and rightNode == None:
                continue
            if leftNode.val != rightNode.val:
                return False
            
            l.append(leftNode.left)
            l.append(leftNode.right)
            r.append(rightNode.right)
            r.append(rightNode.left)
    return True