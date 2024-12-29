# Find the Lexicographically Largest String From the Box I
# O(n^2), O(1), TLE
def answerString(self, word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word
    size = len(word) - numFriends + 1
    def max_lex(w1, w2) -> str:
        l, r = 0, 0
        while l<len(w1) and r<len(w2):
            if w1[l] != w2[r]:
                if w1[l] < w2[r]:
                    return w2
                else:
                    return w1
            l += 1
            r += 1
        if l < len(w1):
            return w1
        return w2
    res = ""
    for curr_size in range(1, size+1):
        for i in range(len(word)-curr_size+1):
            if res == "":
                res = word[i:i+curr_size]
            curr = word[i:i+curr_size]
            res = max_lex(res, curr)
    return res