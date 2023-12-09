# Binary Tree Inorder Traversal
# O(n), O(h)
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
        nonlocal res
        if node != None:
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
    dfs(root)
    return res

# O(n), O(h)
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root == None: return []
    res = []
    stack = []
    curr = root
    while stack or curr:
        
        while curr:
            stack.insert(0, curr)
            curr = curr.left
        curr = stack.pop(0)
        res.append(curr.val)
        curr = curr.right

    return res