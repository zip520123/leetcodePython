# Insert Greatest Common Divisors in Linked List
# O(n), O(1)
def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    def gcd(a,b) -> int:
        if a == 0:
            return b
        return gcd(b % a, a)

    while curr:
        prev = curr
        curr = curr.next
        if curr != None:
            node = ListNode(gcd(prev.val, curr.val))
            prev.next = node
            node.next = curr
    return head