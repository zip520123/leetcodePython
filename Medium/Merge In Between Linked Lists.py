# Merge In Between Linked Lists
# O(n), O(1)
def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    head = ListNode(0, list1)
    curr = head
    start = None

    for i in range(b+1):
        if i == a:
            start = curr 
        curr = curr.next
    end = curr.next
    prev = None
    start.next = list2
    
    curr = list2
    while curr:
        prev = curr
        curr = curr.next
    prev.next = end
    return head.next