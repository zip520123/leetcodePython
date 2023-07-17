# Add Two Numbers II
# O(l1+l2), O(1)
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = node
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    l1, l2 = reverse(l1), reverse(l2)
    head = ListNode()
    curr = head
    carry = 0
    while l1 is not None or l2 is not None:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        newNode = ListNode((val1 + val2 + carry) % 10 )
        carry = (val1 + val2 + carry) // 10
        curr.next = newNode
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        newNode = ListNode(carry)
        curr.next = newNode
    return reverse(head.next)