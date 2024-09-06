# Delete Nodes From Linked List Present in Array
# O(n), O(n)
def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums_set = set()
    for n in nums:
        nums_set.add(n)
    d = ListNode()
    curr = head
    prev = d
    while curr:
        if curr.val not in nums_set:
            prev.next = curr
            prev = prev.next
        temp = curr.next
        curr.next = None
        curr = temp
    return d.next