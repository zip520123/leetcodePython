# Convert Binary Search Tree to Sorted Doubly Linked List
# O(n), O(n)
def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if root == None: return None
    stack = []
    head, prev = None, None
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop(-1)
        if prev != None: 
            prev.right = curr
        curr.left = prev
        
        if head == None:
            head = curr
        prev = curr
        curr = curr.right
    
    head.left = prev
    prev.right = head
    return head

# O(n), O(n)
def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if root == None: return None
    head, prev = None, None
    
    def dfs(node: 'Optional[Node]'):
        nonlocal head, prev
        if node == None: return
        dfs(node.left)
        if head == None: head = node
        node.left = prev
        if prev != None: 
            prev.right = node
        prev = node
        dfs(node.right)
    dfs(root)
    head.left = prev
    prev.right = head
    return head