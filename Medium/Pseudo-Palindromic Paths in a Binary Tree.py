# Pseudo-Palindromic Paths in a Binary Tree
# O(n), O(h)
def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node: Optional[TreeNode], path: dict):
        if node == None: return
        nonlocal res
        currPath = path.copy()
        currPath[node.val] += 1
        if node.left == None and node.right == None:
            odd = 0
            for (_, val) in currPath.items():
                if val % 2 == 1: odd += 1
            if odd <= 1: res += 1
        dfs(node.left, currPath)
        dfs(node.right, currPath)
    dfs(root, defaultdict(int))
    return res
