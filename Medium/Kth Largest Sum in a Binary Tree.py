# Kth Largest Sum in a Binary Tree
# O(n log n), O(n)
def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
    if root == None: 
        return -1
    queue = [root]
    arr = []
    while queue:
        temp = queue
        queue = []
        curr = 0
        for node in temp:
            curr += node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        arr.append(curr)
    arr.sort()
    if k-1 >= len(arr):
        return -1
    return arr[len(arr)-1-k+1]