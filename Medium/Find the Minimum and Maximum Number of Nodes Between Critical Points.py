# Find the Minimum and Maximum Number of Nodes Between Critical Points
# O(n), O(n)

def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    prev = head
    curr = head.next
    next = curr.next
    i = 1
    arr = []
    while next != None:
        if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
            arr.append(i)
        i += 1
        prev = curr
        curr = curr.next
        next = next.next
    if len(arr) < 2:
        return [-1, -1]
    minN = math.inf
    for i in range(len(arr)-1):
        minN = min(minN, arr[i+1] - arr[i])
    maxN = arr[-1] - arr[0]
    return [minN, maxN]

# O(n), O(1)
def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    prev = head
    curr = head.next
    next = curr.next
    i = 1
    prev_index = None
    first_index = None
    minN = math.inf
    while next != None:
        if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
            if prev_index != None:
                minN = min(minN, i - prev_index)
            prev_index = i
            if first_index == None:
                first_index = i
        i += 1
        prev = curr
        curr = curr.next
        next = next.next
    if minN == math.inf:
        return [-1, -1]
    maxN = prev_index - first_index
    return [minN, maxN]

