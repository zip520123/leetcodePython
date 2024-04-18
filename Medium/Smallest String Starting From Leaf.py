# Smallest String Starting From Leaf
# O(n), O(n)
def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    res = None
    alpha = [chr(i) for i in range(ord("a"), ord("z")+1)]
    
    def dfs(path: str, node: Optional[TreeNode]):
        if node == None: return
        nonlocal res
        curr = alpha[node.val] + path
        if node.left == None and node.right == None:
            if res == None:
                res = curr
            else:
                l, r = 0, 0
                while l<len(res) and r<len(curr):
                    if res[l] > curr[r]:
                        res = curr
                        return
                    if res[l] < curr[r]:
                        return
                    if res[l] == curr[r]:
                        l += 1
                        r += 1
                if len(curr) < len(res):
                    res = curr
                
        dfs(curr, node.left)
        dfs(curr, node.right)
    dfs("", root)
    return res