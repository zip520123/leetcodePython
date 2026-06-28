# Construct Binary Tree from Inorder and Postorder Traversal
# O(n^2), O(n)
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if len(inorder) == 0:
        return None
    root = postorder[-1]
    i = 0
    while inorder[i] != root:
        i += 1
    
    rootNode = TreeNode(root)
    rootNode.left = self.buildTree(inorder[:i], postorder[:i])
    rootNode.right = self.buildTree(inorder[i+1:], postorder[i:-1])
    return rootNode

# O(n), O(n)
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    memo = { }
    n = len(inorder)
    for i in range(len(inorder)):
        memo[inorder[i]] = i

    def build(in_left, in_right, post_left, post_right) -> Optional[TreeNode]:
        if in_left > in_right:
            return None
        root = postorder[post_right]
        mid = memo[root]
        node = TreeNode(root)
        left_size = mid - in_left
        node.left = build(in_left, mid-1, post_left, post_left + left_size - 1)
        node.right = build(mid + 1, in_right, post_left + left_size, post_right-1 )
        return node


    return build(0, n-1, 0, n-1)