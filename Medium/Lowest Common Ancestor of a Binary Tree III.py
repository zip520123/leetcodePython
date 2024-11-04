# Lowest Common Ancestor of a Binary Tree III
# O(n), O(h)
def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    root = p
    while root.parent != None:
        root = root.parent
    
    def dfs(node: 'Node') -> 'Node':
        if node == None: return None
        if node == p or node == q: return node
        left = dfs(node.left)
        right = dfs(node.right)
        if left != None and right != None: return node
        if left == None and right == None: return None
        if left != None: return left
        return right
    return dfs(root)

def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    root = p
    while root.parent != None:
        root = root.parent

    def dfs(node) -> 'Node':
        if node == None:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        left = dfs(node.left)
        right = dfs(node.right)
        if left == None and right == None:
            return None
        if left and right:
            return node
        if left:
            return left
        if right:
            return right
        return node
    
    return dfs(root)