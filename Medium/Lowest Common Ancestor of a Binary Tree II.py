# Lowest Common Ancestor of a Binary Tree II
# O(n), O(n)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    findP = False
    findQ = False
    def dfs(root: TreeNode) -> TreeNode:
        nonlocal findQ, findP
        if root == None: return None
        left = dfs(root.left)
        right = dfs(root.right)
        if root == p:
            findP = True
            return root
        if root == q: 
            findQ = True
            return root
        if left != None and right != None: return root
        if left == None and right == None: return None
        if left != None: return left
        return right
    node = dfs(root)
    if findP and findQ:
        return node
    return None