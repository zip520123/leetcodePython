# Step-By-Step Directions From a Binary Tree Node to Another
# O(n), O(n)
def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    graph = {}
    def dfs(node: Optional[TreeNode]):
        if node == None: return
        nonlocal graph
        if node.val not in graph:
            graph[node.val] = [None, None, None]
        if node.left != None:
            graph[node.val][1] = node.left.val
            if node.left.val not in graph:
                graph[node.left.val] = [node.val, None, None]
            dfs(node.left)
        if node.right != None:
            graph[node.val][2] = node.right.val
            if node.right.val not in graph:
                graph[node.right.val] = [node.val, None, None]
            dfs(node.right)
    dfs(root)

    queue = [(startValue, "")]
    seen = set()
    seen.add(startValue)
    while queue:
        temp = queue
        queue = []
        for node, path in temp:
            if node == destValue: return path
            if node in graph:
                parent, left, right = graph[node]
                if parent not in seen:
                    seen.add(parent)
                    queue.append((parent, path+"U"))
                if left not in seen:
                    seen.add(left)
                    queue.append((left, path+"L"))
                if right not in seen:
                    seen.add(right)
                    queue.append((right, path+"R"))
    return ""