# Swap Nodes in Pairs
# O(n) time, O(1) space
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    if node is None:
        return None
    next = node.next
    if next is not None:
        nextNext = next.next
        node.next = self.swapPairs(nextNext)
        next.next = node
        return next
    else:
        return node
