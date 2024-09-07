# Linked List in Binary Tree
# O(n^2), O(n)
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    def dfs(node, listNode) -> bool:
        if listNode == None: return True
        if node == None: return False
        res = False
        if listNode.val == node.val:
            res = res or dfs(node.left, listNode.next) or dfs(node.right, listNode.next)
            
        res |= dfs(node.left, listNode)
        res |= dfs(node.right, listNode)
        return res
    return dfs(root, head)

# O(n), O(n)
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    def dfs(node, listNode) -> bool:
        if listNode == None: return True
        if node == None: return False

        if listNode.val == node.val:
            return dfs(node.left, listNode.next) or dfs(node.right, listNode.next)
        else:
            return False
        
    
    def dfs_root(node) -> bool:
        if node == None: 
            return False
        if node.val == head.val:
            if dfs(node, head):
                return True
        return dfs_root(node.left) or dfs_root(node.right)
        
    return dfs_root(root)