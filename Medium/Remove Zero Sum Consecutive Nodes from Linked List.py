# Remove Zero Sum Consecutive Nodes from Linked List
# O(n^2), O(1)
def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    root = ListNode(0, head)
    curr = root
    while curr:
        prefix_sum = 0
        end = curr.next
        while end:
            prefix_sum += end.val
            if prefix_sum == 0:
                curr.next = end.next
            end = end.next
        curr = curr.next
    return root.next


# O(n), O(n)
def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    root = ListNode(0, head)
    prefixSumToNode = {}

    prefixSum = 0
    curr = root
    while curr:
        prefixSum += curr.val
        prefixSumToNode[prefixSum] = curr
        curr = curr.next
    
    curr = root
    prefixSum = 0
    while curr:
        prefixSum += curr.val
        curr.next = prefixSumToNode[prefixSum].next
        curr = curr.next
    return root.next