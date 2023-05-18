# Maximum Twin Sum of a Linked List
# O(n) time, O(n) space
def pairSum(self, head: Optional[ListNode]) -> int:
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    n = len(arr)
    res = 0
    for i in range(0,int(n/2)):
        res = max(res, arr[i]+arr[n-i-1])
    return res

# O(n) time, O(1) space
def pairSum(self, head: Optional[ListNode]) -> int:
    fast = head
    slow = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    curr = mid
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    res = 0
    curr = head
    while prev is not None:
        res = max(res,prev.val+curr.val)
        prev = prev.next
        curr = curr.next
    return res