# Diameter of Binary Tree
# O(n), O(n)
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if root == None: return 0
    graph = defaultdict(list)

    def dfs(root):
        if root == None: return
        if root.left != None:
            graph[root].append(root.left)
            graph[root.left].append(root)
            dfs(root.left)
        if root.right != None:
            graph[root].append(root.right)
            graph[root.right].append(root)
            dfs(root.right)
    dfs(root)

    def bfs(root) -> TreeNode:
        q = [root]
        prev = None
        seen = set()
        seen.add(root)
        while q:
            temp = q
            q = []
            for node in temp:
                prev = node
                for nextNode in graph[node]:
                    if nextNode not in seen:
                        seen.add(nextNode)
                        q.append(nextNode)
        return prev
    node1 = bfs(root)
    node2 = bfs(node1)
    seen = set()
    q = [node1]
    res = 0
    while q:
        temp = q
        q = []
        
        for node in temp:
            if node == node2: return res
            for nextNode in graph[node]:
                if nextNode not in seen:
                    seen.add(nextNode)
                    q.append(nextNode)
        res += 1
    return 0

# O(n), O(n)
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node) -> int:
        if node == None: return 0    
        nonlocal res
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)
        return max(left, right) + 1
    dfs(root)
    return res