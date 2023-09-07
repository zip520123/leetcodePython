# Split Linked List in Parts
# O(n), O(1)
def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    curr = head
    allCount = 0
    while curr != None:
        allCount += 1
        curr = curr.next
    n = allCount // k
    res = []
    curr = head
    for i in range(k):
        currCount = n
        if i < allCount % k:
            currCount += 1
        prev = None
        res.append(curr)
        for _ in range(currCount):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = None
    return res