# Remove Nth Node From End of List
# O(n), O(1)
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    total = 0
    while curr != None:
        total += 1
        curr = curr.next

    root = ListNode()
    root.next = head
    curr = root
    for _ in range(total-n):
        curr = curr.next
    if curr.next != None:
        curr.next = curr.next.next
    return root.next