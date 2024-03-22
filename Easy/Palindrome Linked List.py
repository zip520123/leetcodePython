# Palindrome Linked List
# O(n), O(1)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    curr = slow.next
    slow.next = None
    
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    node1, node2 = head, prev
    while node1 and node2:
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next
    return True