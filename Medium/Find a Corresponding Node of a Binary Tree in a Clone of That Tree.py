#Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#O(n), O(n)

def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def dfs(o: TreeNode, c: TreeNode) -> TreeNode:
        if o:
            if o is target:
                return c
            left = dfs(o.left, c.left)
            if left is not None:
                return left
            right = dfs(o.right, c.right)
            if right is not None:
                return right
        return None
    
    return dfs(original, cloned)