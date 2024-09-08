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

# O(n), O(1)
def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    res = []
    num_of_nodes = count // k
    remain_nodes = count % k
    curr = head
    for i in range(k):
        root = curr
        prev = None
        for _ in range(num_of_nodes):
            prev = curr
            curr = curr.next
        if i < remain_nodes:
            prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        res.append(root)
    return res