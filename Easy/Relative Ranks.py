# Relative Ranks
# O(n log n), O(n)
def findRelativeRanks(self, score: List[int]) -> List[str]:
    score_to_index = {}
    arr = sorted(score, reverse=True)
    for i in range(len(arr)):
        curr = arr[i]
        score_to_index[curr] = i
    res = []
    for curr in score:
        index = score_to_index[curr]
        if index == 0:
            res.append("Gold Medal")
        elif index == 1:
            res.append("Silver Medal")
        elif index == 2:
            res.append("Bronze Medal")
        else:
            res.append(str(index+1))
    return res