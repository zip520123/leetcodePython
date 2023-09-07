# Reverse Linked List II
# O(n), O(1)
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if head == None: return None
    d = ListNode(0, head)
    prev = d
    for _ in range(left-1):
        prev = prev.next
    start = prev.next
    end = start.next
    for _ in range(right-left):
        start.next = end.next
        end.next = prev.next
        prev.next = end
        end = start.next
    return d.next