# Candy
# O(n), O(n)
def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    arr = [1 for _ in range(n)]
    for i in range(n-1):
        if ratings[i] < ratings[i+1]:
            arr[i+1] = arr[i] + 1
    for i in range(n-1,0,-1):
        if ratings[i-1] > ratings[i]:
            arr[i-1] = max(arr[i-1], arr[i]+1)
    return sum(arr) 