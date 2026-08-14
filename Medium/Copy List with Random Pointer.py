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

# O(n), O(1)
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return 
    curr = head
    while curr:
        temp = curr.next
        curr.next = Node(curr.val, temp)
        curr = temp
    curr = head
    while curr:
        cloneNode = curr.next
        if curr.random:
            cloneNode.random = curr.random.next
        curr = curr.next.next
    curr = head
    res = curr.next
    while curr:
        temp = curr.next.next
        cloneNode = curr.next
        if cloneNode.next:
            cloneNode.next = cloneNode.next.next
        curr = temp
    return res