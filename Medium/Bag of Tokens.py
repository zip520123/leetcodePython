# Bag of Tokens
# O(n log n), O(n)
def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    res = 0
    tokens.sort()
    l, r = 0, len(tokens)-1
    score = 0
    while l<=r:
        if power >= tokens[l]:
            power -= tokens[l]
            score += 1
            l += 1
        else:
            if score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                return res
        res = max(res, score)
    return res