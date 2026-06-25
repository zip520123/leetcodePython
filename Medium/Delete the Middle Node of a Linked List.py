# Delete the Middle Node of a Linked List
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next == None:
        return None
    dummy = ListNode(next=head)
    slow = dummy
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head