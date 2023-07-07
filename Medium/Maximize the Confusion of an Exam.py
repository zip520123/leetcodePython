# Maximize the Confusion of an Exam
# O(n), O(1)
def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    res = 0; count = k
    l,r = 0,0
    n = len(answerKey)
    while r<n:
        if answerKey[r] == "T":
            count -= 1
            while count < 0:
                if answerKey[l] == "T":
                    count += 1
                l += 1
        res = max(res, r-l+1)
        r += 1
    l=0;r=0;count=k
    while r<n:
        if answerKey[r] == "F":
            count -= 1
            while count < 0:
                if answerKey[l] == "F":
                    count += 1
                l += 1
        res = max(res, r-l+1)
        r += 1
    return res