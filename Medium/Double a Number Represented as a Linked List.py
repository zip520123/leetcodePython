# Double a Number Represented as a Linked List
# O(n), O(1)
def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    newHead = self.revert(head)
    carry = 0
    prev = None
    curr = newHead
    while curr:
        val = curr.val * 2 + carry
        curr.val = val % 10
        carry = val // 10
        prev = curr
        curr = curr.next
    if carry > 0:
        prev.next = ListNode(carry)
    return self.revert(newHead)


def revert(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev