# Count Number of Teams
# O(n^2), O(1)
def numTeams(self, rating: List[int]) -> int:
    res = 0
    n = len(rating)
    
    for j in range(n):

        leftLess = leftGreater = rightLess = rightGreater = 0
        for i in range(j):
            if rating[i] < rating[j]:
                leftLess += 1
            elif rating[i] > rating[j]:
                leftGreater += 1
        for k in range(j+1,n):
            if rating[j] < rating[k]:
                rightGreater += 1
            elif rating[j] > rating[k]:
                rightLess += 1
        res += leftLess * rightGreater + leftGreater * rightLess
    return res