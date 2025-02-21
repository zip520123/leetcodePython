# Find Elements in a Contaminated Binary Tree
# O(n), O(n)
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.n_set = set()
        def dfs(node):
            if node == None:
                return
            self.n_set.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)
        root.val = 0
        dfs(root)
            

    def find(self, target: int) -> bool:
        return target in self.n_set