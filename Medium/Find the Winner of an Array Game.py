# Find the Winner of an Array Game
# O(n), O(n), queue
def getWinner(self, arr: List[int], k: int) -> int:
    queue = arr
    maxN = max(arr)
    curr = queue.pop(0)
    wins = 0
    while 1:
        opponent = queue.pop(0)
        if curr > opponent:
            wins += 1
        else:
            queue.append(curr)
            curr = opponent
            wins = 1
        if wins == k or curr == maxN: 
            return curr
        
# O(n), O(1)
def getWinner(self, arr: List[int], k: int) -> int:
    maxN = max(arr)
    curr = arr[0]
    wins = 0

    for i in range(1,len(arr)):
        opponent = arr[i]
        if curr > opponent:
            wins += 1
        else :
            curr = opponent
            wins = 1
        if wins == k or curr == maxN: return curr
    