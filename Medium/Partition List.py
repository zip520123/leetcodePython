# Partition List
# O(n), O(1)
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    l, r = ListNode(), ListNode()
    lHead, rHead = l, r
    curr = head
    while curr is not None:
        if curr.val < x:
            l.next = curr
            curr = curr.next
            l = l.next
            l.next = None
        else:
            r.next = curr
            curr = curr.next
            r = r.next
            r.next = None
    l.next = rHead.next
    return lHead.next