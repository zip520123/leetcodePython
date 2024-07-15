# Create Binary Tree From Descriptions
# O(n), O(n)
def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    memo = {}
    parents = {}
    for parent, child, isleft in descriptions:
        if parent not in memo:
            memo[parent] = TreeNode(parent)
        if child not in memo:
            memo[child] = TreeNode(child)
        if isleft == 1:
            memo[parent].left = memo[child]
        else:
            memo[parent].right = memo[child]
        parents[child] = parent
    for node, _, _ in descriptions:
        if node not in parents:
            return memo[node]