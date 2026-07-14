# Populating Next Right Pointers in Each Node II
# O(n), O(1)
def connect(self, root: 'Node') -> 'Node':
    curr = root
    while curr:
        head = None
        tail = None
        while curr:
            for child in [curr.left, curr.right]:
                if child == None:
                    continue
                if head == None:
                    head = child
                    tail = child
                else:
                    tail.next = child
                    tail = child
            curr = curr.next
        curr = head
    return root