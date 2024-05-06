# Remove Nodes From Linked List
# O(n), O(n)
def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(math.inf)
    queue = [dummy]
    curr = head
    while curr:
        while queue and queue[-1].val < curr.val:
            queue.pop(-1)
        queue.append(curr)
        curr = curr.next
        
    prev = dummy
    for i in range(1, len(queue)):
        prev.next = queue[i]
        prev = prev.next
    return dummy.next