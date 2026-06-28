# Odd Even Linked List
# O(n), O(1)
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return None
    odd = head
    even = head.next
    even_head = head.next
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next
    odd.next = even_head

    return head