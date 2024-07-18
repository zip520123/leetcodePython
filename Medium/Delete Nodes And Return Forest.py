# Delete Nodes And Return Forest
# O(n), O(n)
def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    delete_set = set()
    for n in to_delete:
        delete_set.add(n)
    res = []
    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None: return None
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        if node.val in delete_set:
            if node.left != None:
                res.append(node.left)
            if node.right != None:
                res.append(node.right)
            return None
        return node
    if root != None and root.val not in delete_set:
        res.append(root)
    dfs(root)

    return res