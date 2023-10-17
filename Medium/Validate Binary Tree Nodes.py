# Validate Binary Tree Nodes
# O(e+v), O(e)
def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    memo = {}
    for i in range(n):
        memo[i] = i
    def find(n: int)-> int:
        if memo[n] == n: return n
        memo[n] = find(memo[n])
        return memo[n]
    def union(n1,n2):
        root1, root2 = find(n1), find(n2)
        memo[root2] = root1
    
    for i in range(n):
        left = leftChild[i]
        if left != -1: union(i, left)
        right = rightChild[i]
        if right != -1: union(i, right)
    root = find(0)
    seen = set()
    seen.add(root)
    queue = [root]
    while queue:
        node = queue.pop()
        left = leftChild[node]
        if left != -1:
            if left in seen: return False
            seen.add(left)
            queue.append(left)
        right = rightChild[node]
        if right != -1:
            if right in seen: return False
            seen.add(right)
            queue.append(right)
    for i in range(n):
        if i not in seen: return False
    return True