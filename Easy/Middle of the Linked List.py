# Middle of the Linked List
# O(n), O(1)
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    curr = head
    for _ in range(count//2):
        curr = curr.next
    return curr

# O(n), O(1)
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow