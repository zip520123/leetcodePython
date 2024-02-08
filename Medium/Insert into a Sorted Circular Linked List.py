# Insert into a Sorted Circular Linked List
# O(n), O(1)
def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
    newNode = Node(insertVal)
    if head == None: 
        newNode.next = newNode
        return newNode
    curr = head
    while True:
        if curr.val <= insertVal and insertVal <= curr.next.val:
            break
        if curr.val > curr.next.val:
            if curr.val <= insertVal or insertVal <= curr.next.val:
                break
        curr = curr.next
        if curr is head:
            break
    temp = curr.next
    curr.next = newNode
    newNode.next = temp
    return head