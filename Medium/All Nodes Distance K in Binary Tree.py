# All Nodes Distance K in Binary Tree
# O(n), O(n)
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    graph = defaultdict(list)
    queue = [root]
    while queue:
        temp = queue
        queue = []
        for node in temp:
            if node.left is not None:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)
    queue2 = [target.val]
    seens = set()
    seens.add(target.val)
    for _ in range(k):
        temp = queue2
        queue2 = []
        for node in temp:
            for next in graph[node]:
                if next not in seens:
                    seens.add(next)
                    queue2.append(next)
    return queue2