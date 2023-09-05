# Copy List with Random Pointer
# O(n), O(n)
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if head == None: return None
    memo = {}
    curr = head
    while curr != None:
        memo[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr != None:
        node = memo[curr]
        if curr.next in memo:
            node.next = memo[curr.next]
        if curr.random in memo:
            node.random = memo[curr.random]
        curr = curr.next
    return memo[head]