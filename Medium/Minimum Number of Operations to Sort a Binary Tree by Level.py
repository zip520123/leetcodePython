# Minimum Number of Operations to Sort a Binary Tree by Level
def minimumOperations(self, root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    res = 0
    queue = [root]

    while queue:
        temp = queue
        queue = []
        arr = list(map(lambda node: node.val, temp))
        index_map = {}
        for i in range(len(arr)):
            index_map[arr[i]] = i
        sorted_arr = sorted(arr)
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                res += 1
                index1 = i
                index2 = index_map[sorted_arr[i]]
                arr[index1], arr[index2] = arr[index2], arr[index1]
                index_map[arr[index2]] = index2
                index_map[arr[index1]] = index1

        for node in temp:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return res