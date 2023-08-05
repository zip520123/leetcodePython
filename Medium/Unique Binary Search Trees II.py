# Unique Binary Search Trees II
# O(n!), O(n!)
def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

    def dfs(l: int, r: int) -> List[Optional[TreeNode]]:
        if l > r: return [None]
        res = []
        for i in range(l,r+1):
            left = dfs(l,i-1)
            right = dfs(i+1,r)
            for lnode in left:
                for rnode in right:
                    node = TreeNode(i,lnode,rnode)
                    res.append(node)
        return res
    
    return dfs(1,n)
