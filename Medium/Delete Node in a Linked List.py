# Delete Node in a Linked List
# O(n), O(1)
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    curr = node
    prev = None
    while curr != None and curr.next != None:
        prev = curr
        curr.val = curr.next.val
        curr = curr.next
    prev.next = None