# Balance a Binary Search Tree
# O(n), O(n)
def balanceBST(self, root: TreeNode) -> TreeNode:
    arr = []
    def dfs(node):
        if node == None: return
        dfs(node.left)
        arr.append(node)
        dfs(node.right)
    
    dfs(root)

    def dfs(l, r) -> TreeNode:
        if l > r: return None
        i = (l+r) // 2
        node = arr[i]
        node.left = dfs(l, i-1)
        node.right = dfs(i+1, r)
        return node
    return dfs(0, len(arr)-1)