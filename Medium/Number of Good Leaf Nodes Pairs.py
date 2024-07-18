# Number of Good Leaf Nodes Pairs
# O(n*d^2), O(n)
def countPairs(self, root: TreeNode, distance: int) -> int:
    res = 0
    parents = {}
    leafs = []
    def dfs(parent: Optional[TreeNode], node: Optional[TreeNode]):
        if node == None: return
        parents[node] = parent
        dfs(node, node.left)
        dfs(node, node.right)
        if node.left == None and node.right == None:
            leafs.append(node)
    dfs(None, root)
    
    for leaf in leafs:
        queue = [leaf]
        steps = 0
        seen = set()
        seen.add(leaf)
        while queue and steps <= distance:
            temp = queue
            queue = []
            steps += 1
            for node in temp:
                if node.left == None and node.right == None and node != leaf:
                    res += 1
                if node.left != None and node.left not in seen:
                    seen.add(node.left)
                    queue.append(node.left)
                    
                if node.right != None and node.right not in seen:
                    seen.add(node.right)
                    queue.append(node.right)
                if node in parents and parents[node] != None:
                    parent = parents[node]
                    if parent not in seen:
                        seen.add(parent)
                        queue.append(parent)
    return res // 2