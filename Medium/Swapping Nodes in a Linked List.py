# Swapping Nodes in a Linked List
# O(n) time, O(1) space
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    count = 0
    curr = head
    left = ListNode()
    while curr is not None:
        count += 1
        if count == k:
            left = curr
        curr = curr.next
    right = ListNode()
    fromEnd = count-k
    curr = head
    for _ in range(0,fromEnd):
        curr = curr.next
    right = curr
    temp = left.val
    left.val = right.val
    right.val = temp
    return head
            